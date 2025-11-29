# Species Conservation Status Checker

This script uses the IUCN Red List API client to check the conservation status of species from a CSV or Excel file. All conservation status descriptions and categories are fetched dynamically from the IUCN API in real-time.

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
# Display results as table in console
python check_species_status.py input_file.csv

# Save as CSV
python check_species_status.py input_file.csv -o output.csv

# Save as TSV
python check_species_status.py input_file.csv -o output.tsv

# Save as Excel
python check_species_status.py input_file.csv -o output.xlsx

# Show detailed progress with verbose flag
python check_species_status.py input_file.csv -v
python check_species_status.py input_file.csv --verbose -o output.csv
```

**Note:** By default, the script only displays results. Use the `--verbose` or `-v` flag to see:
- Progress messages while checking each species
- Summary statistics (total checked, found, not found, errors)
- List of threatened species with study links

### Output Formats

- **Table**: Display results in console (default when no output file specified)
- **CSV**: Comma-separated values (`.csv`)
- **TSV**: Tab-separated values (`.tsv`)
- **Excel**: Excel workbook (`.xlsx` or `.xls`)

### Input File Format

The script accepts CSV or Excel files with one of these column structures:

**Option 1: Single species column**
```csv
species,common_name,location
Quercus alba,White Oak,North America
Panthera leo,Lion,Africa
Dionaea muscipula,Venus Flytrap,North Carolina
```

**Option 2: Separate genus and species columns**
```csv
genus,species_name,common_name
Quercus,alba,White Oak
Panthera,leo,Lion
Gorilla,beringei,Eastern Gorilla
```

**Supported column names:**
- `species`, `scientific_name`, or `name` for full scientific names
- `genus` for genus names
- `species_name` or `epithet` for species epithets

## Output

The script generates a detailed report including:

- **Conservation Status**: IUCN Red List category code (EX, CR, EN, VU, NT, LC, etc.)
- **Status Description**: Human-readable status fetched from API (Extinct, Critically Endangered, etc.)
- **Threat Level**: Boolean indicating if species is threatened
- **Assessment Year**: Year the assessment was published
- **Assessment ID**: Unique identifier for the study
- **Study URL**: Link to the full assessment on IUCN Red List website
- **Extinction Flags**: Possibly extinct or possibly extinct in wild indicators

All status descriptions are retrieved dynamically from the IUCN Red List API to ensure accuracy.

### Example Output

**Default output (table only):**
```
       scientific_name                  common_name     family_name   conservation_status  is_threatened year_published assessment_id                                                     url
          Quercus alba                    White Oak        FAGACEAE         Least Concern          False           2015       2295268      https://www.iucnredlist.org/species/194051/2295268
  Sequoia sempervirens                      Redwood    CUPRESSACEAE            Endangered           True           2013       2841558       https://www.iucnredlist.org/species/34051/2841558
```

**Verbose output (with --verbose flag):**
```
Fetching conservation status descriptions from API...
Loaded 7 species from sample_species.csv

Checking species status...
Checking Quercus alba...
Checking Sequoia sempervirens...

=== SUMMARY ===
Total species checked: 7
Found in IUCN database: 6
Not found: 1
Errors: 0

=== THREATENED SPECIES (2) ===
• Sequoia sempervirens: Endangered (2013)
  Study: https://www.iucnredlist.org/species/34051/2841558
• Acaena exigua: Extinct (2016)
  Study: https://www.iucnredlist.org/species/44072/101442020

=== RESULTS TABLE ===
[table output here]
```

### Output Columns

The output includes the following columns:
- `scientific_name`: Species scientific name
- `common_name`: Primary common name (e.g., "Venus Flytrap")
- `family_name`: Taxonomic family
- `conservation_status`: Human-readable IUCN status (e.g., "Vulnerable", "Endangered")
- `is_threatened`: Boolean indicating if species is threatened
- `year_published`: Assessment publication year
- `assessment_id`: Unique assessment identifier
- `url`: Link to full assessment

All status values use full descriptions (e.g., "Vulnerable" instead of "VU") fetched from the API.

## Sample Usage

```bash
# Display results as table
python check_species_status.py sample_species.csv

# Display with progress messages
python check_species_status.py sample_species.csv --verbose

# Save as CSV
python check_species_status.py sample_species.csv -o results.csv

# Save as TSV
python check_species_status.py sample_species.csv -o results.tsv

# Save as Excel with verbose output
python check_species_status.py my_plants.xlsx -o conservation_report.xlsx -v
```

## Conservation Status

Status descriptions are fetched dynamically from the IUCN Red List API and displayed as full text rather than codes. Common statuses include:
- Extinct
- Extinct in the Wild  
- Critically Endangered
- Endangered
- Vulnerable
- Near Threatened
- Least Concern
- Data Deficient
- Not Evaluated

The output uses these full descriptions (e.g., "Vulnerable" instead of "VU") for better readability.

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

- `sample_species.csv`: Example input file with 17 diverse species (plants, mammals, birds, reptiles, amphibians) representing various conservation statuses
- `check_species_status.py`: Main script
- `requirements-species-checker.txt`: Additional Python dependencies

The sample file includes species ranging from Least Concern to Critically Endangered and Extinct, providing a comprehensive demonstration of the tool's capabilities.
