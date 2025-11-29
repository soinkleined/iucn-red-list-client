#!/usr/bin/env python3
"""
Species Conservation Status Checker

This script reads a CSV or Excel file containing plant species names and checks
their conservation status using the IUCN Red List API.

Expected input columns:
- 'species' or 'scientific_name': Full scientific name (e.g., "Quercus alba")
- 'genus': Genus name (optional, will be extracted from species if not provided)
- 'species_name': Species epithet (optional, will be extracted from species if not provided)

Output includes:
- Conservation status (LC, NT, VU, EN, CR, EX, etc.)
- Assessment year
- Assessment URL
- Study/assessment ID
"""

import argparse
import csv
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd
from iucn_red_list_client import IUCNRedListClient


def parse_scientific_name(scientific_name: str) -> Tuple[Optional[str], Optional[str]]:
    """Parse scientific name into genus and species components."""
    parts = scientific_name.strip().split()
    if len(parts) >= 2:
        return parts[0], parts[1]
    elif len(parts) == 1:
        return parts[0], None
    return None, None


def check_species_status(client: IUCNRedListClient, genus: str, species: str) -> Dict:
    """Check conservation status for a species."""
    try:
        response = client.call_endpoint('get_taxa_scientific_name', 
                                      genus_name=genus, 
                                      species_name=species)
        
        if 'assessments' in response and response['assessments']:
            # Get the latest assessment
            latest = None
            for assessment in response['assessments']:
                if assessment.get('latest', False):
                    latest = assessment
                    break
            
            # If no latest found, use the first one
            if not latest and response['assessments']:
                latest = response['assessments'][0]
            
            if latest:
                # Get taxon info
                taxon = response.get('taxon', {})
                
                # Get common name (first main common name if available)
                common_name = 'N/A'
                common_names = taxon.get('common_names', [])
                for cn in common_names:
                    if cn.get('main', False):
                        common_name = cn.get('name', 'N/A')
                        break
                if common_name == 'N/A' and common_names:
                    common_name = common_names[0].get('name', 'N/A')
                
                return {
                    'status': 'found',
                    'scientific_name': taxon.get('scientific_name', f"{genus} {species}"),
                    'common_name': common_name,
                    'family_name': taxon.get('family_name', 'N/A'),
                    'red_list_category': latest.get('red_list_category_code', 'Unknown'),
                    'year_published': latest.get('year_published', 'Unknown'),
                    'assessment_id': latest.get('assessment_id', 'Unknown'),
                    'url': latest.get('url', 'Unknown'),
                    'possibly_extinct': latest.get('possibly_extinct', False),
                    'possibly_extinct_in_wild': latest.get('possibly_extinct_in_the_wild', False)
                }
        
        return {
            'status': 'not_found',
            'scientific_name': f"{genus} {species}",
            'common_name': 'N/A',
            'family_name': 'N/A',
            'red_list_category': 'Not Found',
            'year_published': 'N/A',
            'assessment_id': 'N/A',
            'url': 'N/A',
            'possibly_extinct': False,
            'possibly_extinct_in_wild': False
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'scientific_name': f"{genus} {species}",
            'common_name': 'N/A',
            'family_name': 'N/A',
            'red_list_category': 'Error',
            'year_published': 'N/A',
            'assessment_id': 'N/A',
            'url': 'N/A',
            'possibly_extinct': False,
            'possibly_extinct_in_wild': False,
            'error': str(e)
        }


def get_status_descriptions(client: IUCNRedListClient) -> Dict[str, str]:
    """Fetch all status descriptions from API and return as dict."""
    try:
        response = client.call_endpoint('get_red_list_categories')
        descriptions = {}
        # Get the latest version (3.1) descriptions
        for cat in response.get('red_list_categories', []):
            if cat.get('version') == '3.1':
                code = cat.get('code')
                desc = cat.get('description', {}).get('en', code)
                descriptions[code] = desc
        return descriptions
    except Exception:
        return {}


def is_threatened(code: str) -> bool:
    """Check if species is threatened (extinct, endangered, vulnerable)."""
    threatened_codes = {'EX', 'EW', 'CR', 'EN', 'VU'}
    return code in threatened_codes


def read_input_file(file_path: str) -> pd.DataFrame:
    """Read CSV or Excel file into DataFrame."""
    path = Path(file_path)
    
    if path.suffix.lower() == '.csv':
        return pd.read_csv(file_path)
    elif path.suffix.lower() in ['.xlsx', '.xls']:
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}")


def process_species_list(input_file: str, output_file: Optional[str] = None, verbose: bool = False) -> None:
    """Process species list and check conservation status."""
    
    # Initialize IUCN client
    client = IUCNRedListClient()
    
    # Fetch status descriptions from API once
    if verbose:
        print("Fetching conservation status descriptions from API...")
    status_descriptions = get_status_descriptions(client)
    
    # Read input file
    try:
        df = read_input_file(input_file)
        if verbose:
            print(f"Loaded {len(df)} species from {input_file}")
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)
    
    # Determine column names
    species_col = None
    genus_col = None
    species_name_col = None
    
    for col in df.columns:
        col_lower = col.lower()
        if col_lower in ['species', 'scientific_name', 'name']:
            species_col = col
        elif col_lower == 'genus':
            genus_col = col
        elif col_lower in ['species_name', 'epithet']:
            species_name_col = col
    
    if not species_col and not (genus_col and species_name_col):
        print("Error: Could not find species name columns.")
        print("Expected columns: 'species' or 'scientific_name', or 'genus' + 'species_name'")
        print(f"Found columns: {list(df.columns)}")
        sys.exit(1)
    
    results = []
    
    if verbose:
        print("\nChecking species status...")
    for idx, row in df.iterrows():
        if species_col:
            scientific_name = str(row[species_col]).strip()
            genus, species_name = parse_scientific_name(scientific_name)
        else:
            genus = str(row[genus_col]).strip() if genus_col else None
            species_name = str(row[species_name_col]).strip() if species_name_col else None
        
        if not genus or not species_name:
            if verbose:
                print(f"Row {idx + 1}: Skipping invalid species name")
            continue
        
        if verbose:
            print(f"Checking {genus} {species_name}...")
        result = check_species_status(client, genus, species_name)
        
        # Add original row data
        result.update({
            'row_number': idx + 1,
            'input_genus': genus,
            'input_species': species_name
        })
        
        results.append(result)
    
    # Create results DataFrame
    results_df = pd.DataFrame(results)
    
    # Add human-readable status using cached descriptions
    results_df['status_description'] = results_df['red_list_category'].apply(
        lambda code: status_descriptions.get(code, code)
    )
    results_df['is_threatened'] = results_df['red_list_category'].apply(is_threatened)
    
    # Reorder columns - keep only essential output columns
    column_order = [
        'scientific_name', 'common_name', 'family_name', 'conservation_status', 
        'is_threatened', 'year_published', 'assessment_id', 'url'
    ]
    
    # Rename status_description to conservation_status for clarity
    results_df = results_df.rename(columns={'status_description': 'conservation_status'})
    
    # Select only the columns we want in output
    output_columns = [col for col in column_order if col in results_df.columns]
    results_df = results_df[output_columns]
    
    # Print summary (only if verbose)
    if verbose:
        print(f"\n=== SUMMARY ===")
        print(f"Total species checked: {len(results)}")
        found_count = sum(1 for r in results if r['status'] == 'found')
        not_found_count = sum(1 for r in results if r['status'] == 'not_found')
        error_count = sum(1 for r in results if r['status'] == 'error')
        print(f"Found in IUCN database: {found_count}")
        print(f"Not found: {not_found_count}")
        print(f"Errors: {error_count}")
        
        # Threatened species summary
        threatened = results_df[results_df['is_threatened'] == True]
        if len(threatened) > 0:
            print(f"\n=== THREATENED SPECIES ({len(threatened)}) ===")
            for _, row in threatened.iterrows():
                status_desc = row['conservation_status']
                year = row['year_published']
                url = row['url']
                print(f"• {row['scientific_name']}: {status_desc} ({year})")
                if url != 'N/A':
                    print(f"  Study: {url}")
    
    # Save or display results
    if output_file:
        output_path = Path(output_file)
        ext = output_path.suffix.lower()
        
        if ext == '.csv':
            results_df.to_csv(output_file, index=False)
            print(f"Results saved to: {output_file}")
        elif ext == '.tsv':
            results_df.to_csv(output_file, index=False, sep='\t')
            print(f"Results saved to: {output_file}")
        elif ext in ['.xlsx', '.xls']:
            results_df.to_excel(output_file, index=False)
            print(f"Results saved to: {output_file}")
        else:
            # Default to CSV if unknown extension
            results_df.to_csv(output_file, index=False)
            print(f"Results saved to: {output_file}")
    else:
        # Display as table
        if verbose:
            print("\n=== RESULTS TABLE ===")
        print(results_df.to_string(index=False))


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Check conservation status of species using IUCN Red List API'
    )
    parser.add_argument(
        'input_file',
        help='Input CSV or Excel file containing species names'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file path (.csv, .tsv, .xlsx). If not specified, displays table to console.'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed progress messages'
    )
    
    args = parser.parse_args()
    
    if not Path(args.input_file).exists():
        print(f"Error: Input file '{args.input_file}' not found.")
        sys.exit(1)
    
    try:
        process_species_list(args.input_file, args.output, args.verbose)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
