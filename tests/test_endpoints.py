"""Tests for API endpoints configuration."""

import pytest
from iucn_red_list_client.api_endpoints import API_ENDPOINTS


class TestAPIEndpoints:
    """Test cases for API endpoints configuration."""

    @pytest.mark.unit
    def test_endpoints_exist(self):
        """Test that API endpoints are loaded."""
        assert isinstance(API_ENDPOINTS, dict)
        assert len(API_ENDPOINTS) > 0

    @pytest.mark.unit
    def test_endpoint_structure(self):
        """Test that endpoints have required structure."""
        for name, endpoint in API_ENDPOINTS.items():
            assert isinstance(name, str)
            assert isinstance(endpoint, dict)
            
            # Required fields
            assert 'method' in endpoint
            assert 'path' in endpoint
            assert 'summary' in endpoint
            assert 'description' in endpoint
            assert 'tags' in endpoint
            assert 'path_params' in endpoint
            assert 'query_params' in endpoint
            assert 'requires_auth' in endpoint
            
            # Type checks
            assert isinstance(endpoint['method'], str)
            assert isinstance(endpoint['path'], str)
            assert isinstance(endpoint['summary'], str)
            assert isinstance(endpoint['description'], str)
            assert isinstance(endpoint['tags'], list)
            assert isinstance(endpoint['path_params'], list)
            assert isinstance(endpoint['query_params'], list)
            assert isinstance(endpoint['requires_auth'], bool)

    @pytest.mark.unit
    def test_specific_endpoints_exist(self):
        """Test that expected endpoints exist."""
        expected_endpoints = [
            'get_countries',
            'get_countries_code',
            'get_taxa_scientific_name',
            'get_red_list_categories',
            'get_information_api_version',
            'get_assessment_assessment_id'
        ]
        
        for endpoint in expected_endpoints:
            assert endpoint in API_ENDPOINTS

    @pytest.mark.unit
    def test_query_params_structure(self):
        """Test query parameters have correct structure."""
        for name, endpoint in API_ENDPOINTS.items():
            for param in endpoint['query_params']:
                assert isinstance(param, dict)
                assert 'name' in param
                assert 'required' in param
                assert 'type' in param
                
                assert isinstance(param['name'], str)
                assert isinstance(param['required'], bool)
                assert isinstance(param['type'], str)

    @pytest.mark.unit
    def test_path_params_are_strings(self):
        """Test path parameters are strings."""
        for name, endpoint in API_ENDPOINTS.items():
            for param in endpoint['path_params']:
                assert isinstance(param, str)

    @pytest.mark.unit
    def test_methods_are_valid(self):
        """Test HTTP methods are valid."""
        valid_methods = {'GET', 'POST', 'PUT', 'DELETE', 'PATCH'}
        
        for name, endpoint in API_ENDPOINTS.items():
            assert endpoint['method'] in valid_methods

    @pytest.mark.unit
    def test_paths_start_with_api_v4(self):
        """Test all paths start with /api/v4/."""
        for name, endpoint in API_ENDPOINTS.items():
            assert endpoint['path'].startswith('/api/v4/')

    @pytest.mark.unit
    def test_tags_not_empty(self):
        """Test all endpoints have at least one tag."""
        for name, endpoint in API_ENDPOINTS.items():
            assert len(endpoint['tags']) > 0
            for tag in endpoint['tags']:
                assert isinstance(tag, str)
                assert len(tag) > 0
