#!/usr/bin/env python3
"""
Basic usage examples for IUCN Red List API Client.
"""

from iucn_red_list_client import IUCNRedListClient
import json

def main():
    """Demonstrate basic usage of the IUCN Red List API Client."""
    
    # Initialize client (will use environment variables or config file)
    client = IUCNRedListClient()
    
    print("=== IUCN Red List API Client Examples ===\n")
    
    # Example 1: Get API version information
    print("1. Getting API version information...")
    try:
        version_info = client.call_endpoint('get_information_api_version')
        print(f"API Version: {json.dumps(version_info, indent=2)}\n")
    except Exception as e:
        print(f"Error getting API version: {e}\n")
    
    # Example 2: Get Red List version
    print("2. Getting Red List version...")
    try:
        red_list_version = client.call_endpoint('get_information_red_list_version')
        print(f"Red List Version: {json.dumps(red_list_version, indent=2)}\n")
    except Exception as e:
        print(f"Error getting Red List version: {e}\n")
    
    # Example 3: Get list of countries (first page)
    print("3. Getting list of countries (first page)...")
    try:
        countries = client.call_endpoint('get_countries')
        print(f"Countries (first page): {json.dumps(countries, indent=2)}\n")
    except Exception as e:
        print(f"Error getting countries: {e}\n")
    
    # Example 4: Get species count statistics
    print("4. Getting species count statistics...")
    try:
        stats = client.call_endpoint('get_statistics_count')
        print(f"Species Statistics: {json.dumps(stats, indent=2)}\n")
    except Exception as e:
        print(f"Error getting statistics: {e}\n")
    
    # Example 5: Get Red List categories
    print("5. Getting Red List categories...")
    try:
        categories = client.call_endpoint('get_red_list_categories')
        print(f"Red List Categories: {json.dumps(categories, indent=2)}\n")
    except Exception as e:
        print(f"Error getting categories: {e}\n")

if __name__ == '__main__':
    main()
