"""Tests for the species conservation status checker."""

import pytest
import pandas as pd
from unittest.mock import Mock, patch, mock_open
from pathlib import Path
import sys
import os

# Add examples directory to path for importing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'examples'))

from check_species_status import (
    parse_scientific_name,
    check_species_status,
    get_status_description,
    is_threatened,
    read_input_file
)


class TestSpeciesChecker:
    """Test cases for species conservation status checker."""

    @pytest.mark.unit
    def test_parse_scientific_name_valid(self):
        """Test parsing valid scientific names."""
        genus, species = parse_scientific_name("Quercus alba")
        assert genus == "Quercus"
        assert species == "alba"

    @pytest.mark.unit
    def test_parse_scientific_name_single_word(self):
        """Test parsing single word (genus only)."""
        genus, species = parse_scientific_name("Quercus")
        assert genus == "Quercus"
        assert species is None

    @pytest.mark.unit
    def test_parse_scientific_name_empty(self):
        """Test parsing empty string."""
        genus, species = parse_scientific_name("")
        assert genus is None
        assert species is None

    @pytest.mark.unit
    def test_parse_scientific_name_trinomial(self):
        """Test parsing trinomial name (genus species subspecies)."""
        genus, species = parse_scientific_name("Quercus alba var. minor")
        assert genus == "Quercus"
        assert species == "alba"

    @pytest.mark.unit
    def test_get_status_description(self):
        """Test status code descriptions."""
        assert get_status_description('EX') == 'Extinct'
        assert get_status_description('EN') == 'Endangered'
        assert get_status_description('LC') == 'Least Concern'
        assert get_status_description('UNKNOWN') == 'UNKNOWN'

    @pytest.mark.unit
    def test_is_threatened(self):
        """Test threatened status detection."""
        assert is_threatened('EX') is True
        assert is_threatened('CR') is True
        assert is_threatened('EN') is True
        assert is_threatened('VU') is True
        assert is_threatened('LC') is False
        assert is_threatened('NT') is False

    @pytest.mark.unit
    def test_read_input_file_csv(self, tmp_path):
        """Test reading CSV input file."""
        csv_file = tmp_path / "test.csv"
        csv_content = "species,common_name\nQuercus alba,White Oak\n"
        csv_file.write_text(csv_content)
        
        df = read_input_file(str(csv_file))
        assert len(df) == 1
        assert df.iloc[0]['species'] == 'Quercus alba'

    @pytest.mark.unit
    def test_read_input_file_unsupported(self, tmp_path):
        """Test reading unsupported file format."""
        txt_file = tmp_path / "test.txt"
        txt_file.write_text("some content")
        
        with pytest.raises(ValueError, match="Unsupported file format"):
            read_input_file(str(txt_file))

    @pytest.mark.unit
    @patch('check_species_status.IUCNRedListClient')
    def test_check_species_status_found(self, mock_client_class, sample_assessment_response):
        """Test checking species status when species is found."""
        mock_client = Mock()
        mock_client.call_endpoint.return_value = sample_assessment_response
        mock_client_class.return_value = mock_client
        
        result = check_species_status(mock_client, "Test", "species")
        
        assert result['status'] == 'found'
        assert result['scientific_name'] == 'Test species'
        assert result['red_list_category'] == 'VU'
        assert result['year_published'] == '2020'

    @pytest.mark.unit
    @patch('check_species_status.IUCNRedListClient')
    def test_check_species_status_not_found(self, mock_client_class):
        """Test checking species status when species is not found."""
        mock_client = Mock()
        mock_client.call_endpoint.return_value = {'assessments': []}
        mock_client_class.return_value = mock_client
        
        result = check_species_status(mock_client, "Unknown", "species")
        
        assert result['status'] == 'not_found'
        assert result['red_list_category'] == 'Not Found'

    @pytest.mark.unit
    @patch('check_species_status.IUCNRedListClient')
    def test_check_species_status_error(self, mock_client_class):
        """Test checking species status when API error occurs."""
        mock_client = Mock()
        mock_client.call_endpoint.side_effect = Exception("API Error")
        mock_client_class.return_value = mock_client
        
        result = check_species_status(mock_client, "Test", "species")
        
        assert result['status'] == 'error'
        assert result['red_list_category'] == 'Error'
        assert 'error' in result

    @pytest.mark.unit
    @patch('check_species_status.IUCNRedListClient')
    def test_check_species_status_no_latest_assessment(self, mock_client_class):
        """Test checking species with no latest assessment marked."""
        response = {
            'taxon': {'scientific_name': 'Test species'},
            'assessments': [
                {
                    'year_published': '2020',
                    'latest': False,
                    'red_list_category_code': 'VU',
                    'assessment_id': 67890,
                    'url': 'https://example.com'
                }
            ]
        }
        
        mock_client = Mock()
        mock_client.call_endpoint.return_value = response
        mock_client_class.return_value = mock_client
        
        result = check_species_status(mock_client, "Test", "species")
        
        assert result['status'] == 'found'
        assert result['red_list_category'] == 'VU'  # Should use first assessment
