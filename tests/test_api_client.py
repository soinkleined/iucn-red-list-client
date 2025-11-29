"""Unit tests for the IUCN Red List API client."""

import os
import pytest
from unittest.mock import Mock, patch, mock_open
from pathlib import Path

from iucn_red_list_client import IUCNRedListClient
from iucn_red_list_client.cli import show_endpoint_help


class TestIUCNRedListClient:
    """Test cases for IUCNRedListClient class."""

    @pytest.mark.unit
    def test_init_with_config_file(self, tmp_path, mock_api_token):
        """Test client initialization with config file."""
        config_file = tmp_path / "test_config.json"
        config_data = f'{{"api_token": "{mock_api_token}"}}'
        config_file.write_text(config_data)
        
        client = IUCNRedListClient(config_file=str(config_file))
        assert client.config["api_token"] == mock_api_token

    @pytest.mark.unit
    def test_init_with_kwargs(self, mock_api_token):
        """Test client initialization with kwargs."""
        client = IUCNRedListClient(api_token=mock_api_token)
        assert client.config["api_token"] == mock_api_token

    @pytest.mark.unit
    def test_load_env_config(self, mock_api_token):
        """Test loading configuration from environment variables."""
        with patch.dict(os.environ, {"IUCN_API_TOKEN": mock_api_token}):
            client = IUCNRedListClient()
            assert client.config["api_token"] == mock_api_token

    @pytest.mark.unit
    def test_load_env_config_with_base_url(self, mock_api_token):
        """Test loading configuration with custom base URL."""
        custom_url = "https://custom.api.url"
        with patch.dict(os.environ, {
            "IUCN_API_TOKEN": mock_api_token,
            "IUCN_BASE_URL": custom_url
        }):
            client = IUCNRedListClient()
            assert client.config["api_token"] == mock_api_token
            assert client.config["base_url"] == custom_url

    @pytest.mark.unit
    def test_no_config_found(self):
        """Test client initialization with no configuration."""
        with patch.dict(os.environ, {}, clear=True):
            with patch('pathlib.Path.exists', return_value=False):
                client = IUCNRedListClient()
                assert client.config == {}

    @pytest.mark.unit
    @patch('requests.Session.request')
    def test_make_request_success(self, mock_request, client_with_mock_config, mock_response):
        """Test successful API request."""
        mock_request.return_value = mock_response
        
        response = client_with_mock_config._make_request("GET", "/test/path")
        
        assert response == mock_response
        mock_request.assert_called_once()

    @pytest.mark.unit
    @patch('requests.Session.request')
    def test_make_request_failure(self, mock_request, client_with_mock_config):
        """Test failed API request."""
        mock_request.side_effect = Exception("Network error")
        
        with pytest.raises(Exception, match="Network error"):
            client_with_mock_config._make_request("GET", "/test/path")

    @pytest.mark.unit
    @patch('iucn_red_list_client.client.IUCNRedListClient._make_request')
    def test_call_endpoint_success(self, mock_make_request, client_with_mock_config, mock_response):
        """Test successful endpoint call."""
        mock_response.json.return_value = {"result": "success"}
        mock_make_request.return_value = mock_response
        
        result = client_with_mock_config.call_endpoint('get_countries')
        
        assert result == {"result": "success"}
        mock_make_request.assert_called_once()

    @pytest.mark.unit
    def test_call_endpoint_unknown(self, client_with_mock_config):
        """Test calling unknown endpoint."""
        with pytest.raises(ValueError, match="Unknown endpoint"):
            client_with_mock_config.call_endpoint('unknown_endpoint')

    @pytest.mark.unit
    @patch('iucn_red_list_client.client.IUCNRedListClient._make_request')
    def test_call_endpoint_with_path_params(self, mock_make_request, client_with_mock_config, mock_response):
        """Test endpoint call with path parameters."""
        mock_response.json.return_value = {"result": "success"}
        mock_make_request.return_value = mock_response
        
        result = client_with_mock_config.call_endpoint('get_countries_code', code='US')
        
        assert result == {"result": "success"}
        mock_make_request.assert_called_once()

    @pytest.mark.unit
    def test_call_endpoint_missing_path_param(self, client_with_mock_config):
        """Test endpoint call with missing required path parameter."""
        with pytest.raises(ValueError, match="Missing required path parameter"):
            client_with_mock_config.call_endpoint('get_countries_code')

    @pytest.mark.unit
    @patch('iucn_red_list_client.client.IUCNRedListClient._make_request')
    def test_call_endpoint_with_query_params(self, mock_make_request, client_with_mock_config, mock_response):
        """Test endpoint call with query parameters."""
        mock_response.json.return_value = {"result": "success"}
        mock_make_request.return_value = mock_response
        
        result = client_with_mock_config.call_endpoint('get_taxa_scientific_name', 
                                                     genus_name='Test', species_name='species')
        
        assert result == {"result": "success"}
        mock_make_request.assert_called_once()

    @pytest.mark.unit
    def test_call_endpoint_missing_required_query_param(self, client_with_mock_config):
        """Test endpoint call with missing required query parameter."""
        with pytest.raises(ValueError, match="Missing required query parameter"):
            client_with_mock_config.call_endpoint('get_taxa_scientific_name', genus_name='Test')


class TestHelperFunctions:
    """Test cases for helper functions."""

    @pytest.mark.unit
    def test_show_endpoint_help_valid_endpoint(self, capsys):
        """Test showing help for valid endpoint."""
        show_endpoint_help('get_countries')
        captured = capsys.readouterr()
        assert 'get_countries:' in captured.out
        assert 'Countries' in captured.out

    @pytest.mark.unit
    def test_show_endpoint_help_invalid_endpoint(self, capsys):
        """Test showing help for invalid endpoint."""
        show_endpoint_help('invalid_endpoint')
        captured = capsys.readouterr()
        # The error message goes to stderr via logger
        assert captured.out == '' or "not found" in captured.out
