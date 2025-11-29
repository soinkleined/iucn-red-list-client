"""Integration tests for the IUCN Red List API client."""

import os
import pytest
from iucn_red_list_client import IUCNRedListClient


@pytest.mark.integration
class TestIUCNRedListIntegration:
    """Integration tests requiring actual API access."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup for integration tests."""
        self.api_token = os.getenv('IUCN_API_TOKEN')
        if not self.api_token:
            pytest.skip("IUCN_API_TOKEN environment variable not set")
        
        self.client = IUCNRedListClient(api_token=self.api_token)

    def test_get_api_version(self):
        """Test getting API version information."""
        result = self.client.call_endpoint('get_information_api_version')
        assert 'api_version' in result
        assert result['api_version'] == 'v4'

    def test_get_countries(self):
        """Test getting list of countries."""
        result = self.client.call_endpoint('get_countries')
        assert isinstance(result, list) or 'result' in result or 'countries' in result
        
        # Check if we have countries data
        countries = result if isinstance(result, list) else result.get('result', result.get('countries', []))
        assert len(countries) > 0
        
        # Check structure of first country
        first_country = countries[0]
        assert 'code' in first_country
        assert 'description' in first_country

    def test_get_red_list_categories(self):
        """Test getting Red List categories."""
        result = self.client.call_endpoint('get_red_list_categories')
        assert 'red_list_categories' in result
        
        categories = result['red_list_categories']
        assert len(categories) > 0
        
        # Check for expected categories
        category_codes = [cat['code'] for cat in categories]
        expected_codes = ['EX', 'EW', 'CR', 'EN', 'VU', 'NT', 'LC']
        for code in expected_codes:
            assert code in category_codes

    def test_get_species_by_scientific_name(self):
        """Test getting species by scientific name."""
        # Test with a known species
        result = self.client.call_endpoint('get_taxa_scientific_name',
                                         genus_name='Panthera',
                                         species_name='leo')
        
        assert 'taxon' in result
        assert result['taxon']['scientific_name'] == 'Panthera leo'
        assert 'assessments' in result

    def test_get_country_assessments(self):
        """Test getting assessments for a specific country."""
        result = self.client.call_endpoint('get_countries_code', code='US')
        
        assert 'country' in result
        assert result['country']['code'] == 'US'
        assert 'assessments' in result

    def test_get_statistics(self):
        """Test getting API statistics."""
        result = self.client.call_endpoint('get_statistics_count')
        
        assert 'count' in result
        assert isinstance(result['count'], int)
        assert result['count'] > 0

    @pytest.mark.slow
    def test_multiple_requests(self):
        """Test making multiple requests to ensure session handling."""
        # Make several requests
        results = []
        endpoints = [
            ('get_information_api_version', {}),
            ('get_red_list_categories', {}),
            ('get_countries', {}),
        ]
        
        for endpoint, params in endpoints:
            result = self.client.call_endpoint(endpoint, **params)
            results.append(result)
        
        # Verify all requests succeeded
        assert len(results) == 3
        assert all(result is not None for result in results)
