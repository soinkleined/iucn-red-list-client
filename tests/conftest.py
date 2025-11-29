"""Test configuration and fixtures."""

import os
import pytest
from unittest.mock import Mock, patch
from iucn_red_list_client import IUCNRedListClient


@pytest.fixture
def mock_api_token():
    """Mock API token for testing."""
    return "test_token_12345"


@pytest.fixture
def mock_config():
    """Mock configuration for testing."""
    return {
        "api_token": "test_token_12345",
        "base_url": "https://api.iucnredlist.org"
    }


@pytest.fixture
def client_with_mock_config(mock_config):
    """Create client with mock configuration."""
    with patch.object(IUCNRedListClient, '_load_config', return_value=mock_config):
        return IUCNRedListClient()


@pytest.fixture
def mock_response():
    """Mock HTTP response."""
    response = Mock()
    response.status_code = 200
    response.json.return_value = {"test": "data"}
    response.raise_for_status.return_value = None
    return response


@pytest.fixture
def sample_assessment_response():
    """Sample assessment response data."""
    return {
        "taxon": {
            "sis_id": 12345,
            "scientific_name": "Test species",
            "kingdom_name": "PLANTAE",
            "genus_name": "Test",
            "species_name": "species"
        },
        "assessments": [
            {
                "year_published": "2020",
                "latest": True,
                "red_list_category_code": "VU",
                "assessment_id": 67890,
                "url": "https://www.iucnredlist.org/species/12345/67890"
            }
        ]
    }


@pytest.fixture
def sample_countries_response():
    """Sample countries response data."""
    return [
        {
            "description": {"en": "United States"},
            "code": "US"
        },
        {
            "description": {"en": "Canada"},
            "code": "CA"
        }
    ]
