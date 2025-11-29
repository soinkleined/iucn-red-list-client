# Species Conservation Status Checker

This script uses the IUCN Red List API client to check the conservation status of plant species from a CSV or Excel file.

## Installation

```bash
# Install the IUCN client package
pip install -e .

# Install additional dependencies for the species checker
pip install -r requirements-species-checker.txt
```

## Setup

Set your IUCN API token:
```bash
export IUCN_API_TOKEN="your_api_token_here"
```

## Usage

```bash
python check_species_status.py input_file.csv [-o output_file.csv]
```

### Input File Format

The script accepts CSV or Excel files with one of these column structures:

**Option 1: Single species column**
```csv
species,common_name,location
Quercus alba,White Oak,North America
Sequoia sempervirens,Coast Redwood,California
```

**Option 2: Separate genus and species columns**
```csv
genus,species_name,common_name
Quercus,alba,White Oak
Sequoia,sempervirens,Coast Redwood
```

**Supported column names:**
- `species`, `scientific_name`, or `name` for full scientific names
- `genus` for genus names
- `species_name` or `epithet` for species epithets

## Output

The script generates a detailed report including:

- **Conservation Status**: IUCN Red List category (EX, CR, EN, VU, NT, LC, etc.)
- **Status Description**: Human-readable status (Extinct, Critically Endangered, etc.)
- **Threat Level**: Boolean indicating if species is threatened
- **Assessment Year**: Year the assessment was published
- **Assessment ID**: Unique identifier for the study
- **Study URL**: Link to the full assessment on IUCN Red List website
- **Extinction Flags**: Possibly extinct or possibly extinct in wild indicators

### Example Output

```
=== SUMMARY ===
Total species checked: 7
Found in IUCN database: 6
Not found: 1
Errors: 0

=== THREATENED SPECIES (2) ===
• Acaena exigua: Extinct (2016)
  Study: https://www.iucnredlist.org/species/44072/101442020
• Encephalartos woodii: Extinct in the Wild (2010)
  Study: https://www.iucnredlist.org/species/41916/10657117
```

## Sample Usage

```bash
# Check species in sample file
python check_species_status.py sample_species.csv

# Specify custom output file
python check_species_status.py my_plants.xlsx -o conservation_report.xlsx
```

## Conservation Status Codes

- **EX**: Extinct
- **EW**: Extinct in the Wild  
- **CR**: Critically Endangered
- **EN**: Endangered
- **VU**: Vulnerable
- **NT**: Near Threatened
- **LC**: Least Concern
- **DD**: Data Deficient
- **NE**: Not Evaluated

## Error Handling

The script handles:
- Missing or invalid species names
- API connection errors
- Species not found in IUCN database
- Invalid file formats

All errors are logged and included in the output report.

## Rate Limiting

The script includes built-in delays to respect IUCN API rate limits. For large datasets, the process may take some time to complete.

## Example Files

- `sample_species.csv`: Example input file with various plant species
- `check_species_status.py`: Main script
- `requirements-species-checker.txt`: Additional Python dependencies
