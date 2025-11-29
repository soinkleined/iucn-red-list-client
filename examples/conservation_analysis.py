#!/usr/bin/env python3
"""
Conservation analysis examples using IUCN Red List API Client.
"""

from iucn_red_list_client import IUCNRedListClient
import json

def analyze_endangered_species(client):
    """Analyze endangered species globally."""
    print("=== Endangered Species Analysis ===")
    
    try:
        # Get all critically endangered species
        print("Getting critically endangered species...")
        critically_endangered = client.call_endpoint('get_red_list_categories_code', code='CR')
        print(f"Total critically endangered species: {len(critically_endangered.get('assessments', []))}")
        
        # Get all endangered species
        print("Getting endangered species...")
        endangered = client.call_endpoint('get_red_list_categories_code', code='EN')
        print(f"Total endangered species: {len(endangered.get('assessments', []))}")
        
        # Get all vulnerable species
        print("Getting vulnerable species...")
        vulnerable = client.call_endpoint('get_red_list_categories_code', code='VU')
        print(f"Total vulnerable species: {len(vulnerable.get('assessments', []))}")
        
        total_threatened = (len(critically_endangered.get('assessments', [])) + 
                          len(endangered.get('assessments', [])) + 
                          len(vulnerable.get('assessments', [])))
        print(f"Total threatened species (CR + EN + VU): {total_threatened}")
        
    except Exception as e:
        print(f"Error in endangered species analysis: {e}")

def analyze_by_habitat(client):
    """Analyze species by habitat type."""
    print("\n=== Habitat Analysis ===")
    
    try:
        # Get list of habitats
        habitats = client.call_endpoint('get_habitats')
        print(f"Total habitat types available: {len(habitats.get('result', []))}")
        
        # Analyze a few key habitats
        key_habitats = [
            ('1_1', 'Forest - Boreal'),
            ('5_1', 'Wetlands - Permanent Rivers/Streams/Creeks'),
            ('9_1', 'Marine Neritic - Pelagic'),
        ]
        
        for code, name in key_habitats:
            try:
                species = client.call_endpoint('get_habitats_code', code=code)
                print(f"Species in {name}: {len(species.get('assessments', []))}")
            except Exception as e:
                print(f"Error getting species for habitat {name}: {e}")
                
    except Exception as e:
        print(f"Error in habitat analysis: {e}")

def analyze_population_trends(client):
    """Analyze species by population trends."""
    print("\n=== Population Trend Analysis ===")
    
    try:
        # Get population trends
        trends = client.call_endpoint('get_population_trends')
        print(f"Available population trends: {json.dumps(trends, indent=2)}")
        
        # Analyze species with decreasing populations
        print("Getting species with decreasing populations...")
        decreasing = client.call_endpoint('get_population_trends_code', code='1')
        print(f"Species with decreasing populations: {len(decreasing.get('assessments', []))}")
        
        # Analyze species with increasing populations
        print("Getting species with increasing populations...")
        increasing = client.call_endpoint('get_population_trends_code', code='0')
        print(f"Species with increasing populations: {len(increasing.get('assessments', []))}")
        
    except Exception as e:
        print(f"Error in population trend analysis: {e}")

def main():
    """Run conservation analysis examples."""
    
    # Initialize client
    client = IUCNRedListClient()
    
    print("=== IUCN Red List Conservation Analysis ===\n")
    
    # Run different analyses
    analyze_endangered_species(client)
    analyze_by_habitat(client)
    analyze_population_trends(client)
    
    print("\n=== Analysis Complete ===")

if __name__ == '__main__':
    main()
