# IUCN Red List API Client Examples

This directory contains example scripts demonstrating various use cases for the IUCN Red List API Client.

## Prerequisites

Before running these examples, make sure you have:

1. Installed the IUCN Red List API Client package
2. Obtained an API token from the IUCN Red List API
3. Set up your configuration (environment variables or config file)

### Setting up Environment Variables

```bash
export IUCN_API_TOKEN="your_api_token_here"
export IUCN_BASE_URL="https://apiv3.iucnredlist.org"  # Optional
```

### Or create a config file

Create `~/.iucn_client.json`:
```json
{
    "api_token": "your_api_token_here",
    "base_url": "https://api.iucnredlist.org"
}
```

See `../config/iucn_client.json.example` for a template.

## Available Examples

### 1. Basic Usage (`basic_usage.py`)

Demonstrates fundamental operations:
- Getting API version information
- Retrieving Red List version
- Listing countries
- Getting species statistics
- Accessing Red List categories

```bash
python examples/basic_usage.py
```

### 2. Species Conservation Status Checker (`check_species_status.py`)

Batch processing script for checking conservation status of multiple species:
- Reads CSV or Excel files with species names
- Queries IUCN Red List API for each species
- Identifies threatened species (Extinct, Endangered, Vulnerable)
- Generates detailed conservation reports with study citations
- Fetches Red List category descriptions dynamically from API
- Supports multiple output formats: table (console), CSV, TSV, Excel
- Clean output by default; use `--verbose` for progress messages and summaries

All status descriptions and categories are retrieved from the API in real-time.

**Additional requirements:**
```bash
pip install -r requirements-species-checker.txt
```

**Usage:**
```bash
# Display as table (clean output)
python examples/check_species_status.py examples/sample_species.csv

# Display with progress and summary (verbose)
python examples/check_species_status.py examples/sample_species.csv --verbose

# Save as CSV
python examples/check_species_status.py examples/sample_species.csv -o results.csv

# Save as TSV
python examples/check_species_status.py examples/sample_species.csv -o results.tsv

# Save as Excel with verbose output
python examples/check_species_status.py examples/sample_species.csv -o results.xlsx -v
```

**Usage:**
```bash
# Check species from CSV file
python check_species_status.py sample_species.csv

# Specify custom output file
python check_species_status.py sample_species.csv -o conservation_report.xlsx
```

**Sample files:**
- `sample_species.csv` - Example input file with plant species
- `SPECIES_CHECKER_README.md` - Detailed documentation for the species checker

**Input file format:**
```csv
species,common_name,location
Quercus alba,White Oak,North America
Sequoia sempervirens,Coast Redwood,California
```

**Output includes:**
- Conservation status (LC, NT, VU, EN, CR, EX, etc.)
- Assessment year and study ID
- Direct links to IUCN Red List studies
- Threat level indicators

## CLI Examples

### Basic CLI Usage

```bash
# Get API version
iucn-client get_information_api_version

# Get all countries
iucn-client get_countries

# Get species for a specific country
iucn-client get_countries_code -p code=US

# Get endangered species
iucn-client get_red_list_categories_code -p code=EN
```

### Advanced CLI Usage

```bash
# Get species by scientific name
iucn-client get_taxa_scientific_name -p genus_name=Panthera -p species_name=leo

# Get marine species
iucn-client get_habitats_code -p code=9

# Get mammal assessments
iucn-client get_comprehensive_groups_name -p name=mammals

# Enable debug logging
iucn-client get_countries --log-level DEBUG
```

## Research Use Cases

### Biodiversity Hotspot Analysis

```bash
# Get all species in tropical forests
iucn-client get_habitats_code -p code=1_6

# Get all island endemic species
iucn-client get_habitats_code -p code=13
```

### Threat Assessment

```bash
# Get species affected by climate change
iucn-client get_threats_code -p code=11.1

# Get species affected by habitat loss
iucn-client get_threats_code -p code=1.1
```

### Conservation Priority Analysis

```bash
# Get all possibly extinct species
iucn-client get_taxa_possibly_extinct

# Get all possibly extinct in the wild species
iucn-client get_taxa_possibly_extinct_in_the_wild
```

## Error Handling

All examples include proper error handling. Common issues:

1. **Authentication errors**: Check your API token
2. **Rate limiting**: The client includes automatic retry logic
3. **Network timeouts**: Increase timeout if needed
4. **Invalid parameters**: Check endpoint documentation

## Extending the Examples

You can extend these examples by:

1. Adding data visualization with matplotlib/plotly
2. Exporting results to CSV/Excel files (see species checker example)
3. Creating automated reports
4. Integrating with GIS systems
5. Building web dashboards
6. Batch processing large species datasets
7. Creating conservation status monitoring systems

## Support

For questions about these examples or the API client:
- Check the main README.md
- Review the IUCN Red List API documentation
- Submit issues to the repository
