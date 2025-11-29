<h1 align="center">IUCN Red List API Client</h1>
<p align="center">A Python package and CLI for interacting with the IUCN Red List API v4.</p>

---

## Overview

This repository provides a comprehensive Python package and command-line tool for accessing the IUCN Red List API v4 with advanced features for conservation research, data extraction, and species assessment analysis.

### Key Features

- **🚀 Easy Installation**: Install from source with `pip install .`
- **🔧 Flexible Configuration**: Environment variables or JSON config files
- **📊 Advanced Querying**: Support for all IUCN Red List API v4 endpoints
- **🛡️ Secure Authentication**: Bearer token authentication with SSL certificate validation
- **📝 Structured Logging**: Configurable log levels for debugging and automation
- **🔁 Error Handling**: Automatic retries and timeout handling for reliable operations
- **📚 Built-in Help**: Comprehensive documentation for all API endpoints
- **🌐 Multi-Environment**: Support for production, staging, and development environments

## Quick Start

```bash
# Install directly from GitHub
pip install git+https://github.com/soinkleined/iucn-red-list-client.git

# Or install from source
git clone https://github.com/soinkleined/iucn-red-list-client.git
cd iucn-red-list-client
pip install .

# Set up environment variables
export IUCN_API_TOKEN="your_api_token_here"
export IUCN_BASE_URL="https://api.iucnredlist.org"  # Optional

# Get species assessment
iucn-client get_assessment_assessment_id -p assessment_id=12345

# Get all countries
iucn-client get_countries

# Get species by country
iucn-client get_countries_code -p code=US

# List all available endpoints
iucn-client --list-endpoints
```

## Installation

### From GitHub (Recommended)

```bash
pip install git+https://github.com/soinkleined/iucn-red-list-client.git
```

### From Source

```bash
git clone https://github.com/soinkleined/iucn-red-list-client.git
cd iucn-red-list-client
pip install .
```

### Development Installation

```bash
git clone https://github.com/soinkleined/iucn-red-list-client.git
cd iucn-red-list-client
pip install -e .
```

## Configuration

### Environment Variables (Recommended)

Set the following environment variables:

```bash
export IUCN_API_TOKEN="your_api_token_here"
export IUCN_BASE_URL="https://api.iucnredlist.org"  # Optional, defaults to this URL
```

### Configuration File

Create a JSON configuration file at `~/.iucn_client.json`:

```json
{
    "api_token": "your_api_token_here",
    "base_url": "https://api.iucnredlist.org"
}
```

Or specify a custom config file:

```bash
iucn-client --config /path/to/config.json get_countries
```

See `config/iucn_client.json.example` for a template.

## API Token

To use the IUCN Red List API, you need to obtain an API token:

1. Visit the [IUCN Red List API website](https://api.iucnredlist.org/)
2. Register for an account
3. Generate an API token
4. Set the token in your environment variables or configuration file

For API documentation, see the [Swagger documentation](https://api.iucnredlist.org/api-docs/index.html).

### Citation Requirement

When using this API, you must cite:

**IUCN 2025. IUCN Red List of Threatened Species. Version 2025-2 <www.iucnredlist.org>**

## Usage

### Command Line Interface

#### Basic Usage

```bash
# Get information about a specific assessment
iucn-client get_assessment_assessment_id -p assessment_id=12345

# Get list of countries
iucn-client get_countries

# Get species assessments for a specific country
iucn-client get_countries_code -p code=US
```

#### Advanced Usage

```bash
# Use custom parameters
iucn-client get_taxa_scientific_name -p genus_name=Panthera -p species_name=leo

# Get comprehensive group assessments
iucn-client get_comprehensive_groups_name -p name=mammals

# Get habitat-based assessments
iucn-client get_habitats_code -p code="1_1"

# Get red list category assessments
iucn-client get_red_list_categories_code -p code=VU
```

#### Available Parameters

Use `-p` or `--param` to pass parameters:

```bash
iucn-client get_countries_code -p code=US -p page=1
```

### Python API

```python
from iucn_red_list_client import IUCNRedListClient

# Initialize client
client = IUCNRedListClient(api_token="your_token_here")

# Get assessment data
assessment = client.call_endpoint('get_assessment_assessment_id', assessment_id=12345)

# Get all countries
countries = client.call_endpoint('get_countries')

# Get species for a country
us_species = client.call_endpoint('get_countries_code', code='US')

# Get species by scientific name
species_data = client.call_endpoint('get_taxa_scientific_name', 
                                   genus_name='Panthera', species_name='leo')
```

## Available Endpoints

The client supports all IUCN Red List API v4 endpoints organized by category:

### Assessment
- `get_assessment_assessment_id` - Get assessment by ID

### Biogeographical Realms
- `get_biogeographical_realms` - List biogeographical realms
- `get_biogeographical_realms_code` - Get assessments by biogeographical realm

### Comprehensive Groups
- `get_comprehensive_groups` - List comprehensive groups
- `get_comprehensive_groups_name` - Get assessments by comprehensive group name

### Conservation Actions
- `get_conservation_actions` - List conservation actions
- `get_conservation_actions_code` - Get assessments by conservation action

### Countries
- `get_countries` - List countries
- `get_countries_code` - Get assessments by country

### Growth Forms
- `get_growth_forms` - List growth forms
- `get_growth_forms_code` - Get assessments by growth form

### Habitats
- `get_habitats` - List habitats
- `get_habitats_code` - Get assessments by habitat

### Population Trends
- `get_population_trends` - List population trends
- `get_population_trends_code` - Get assessments by population trend

### Red List Categories
- `get_red_list_categories` - List red list categories
- `get_red_list_categories_code` - Get assessments by category

### Species/Taxa
- `get_taxa_scientific_name` - Get species by scientific name (genus_name + species_name)
- `get_taxa_sis_sis_id` - Get species by SIS ID

### Information
- `get_information_api_version` - Get API version
- `get_information_red_list_version` - Get Red List version

And many more! Use `iucn-client --list-endpoints` to see all available endpoints.

## Error Handling

The client includes robust error handling:

- **Automatic Retries**: Failed requests are automatically retried with exponential backoff
- **Timeout Handling**: Configurable request timeouts (default: 30 seconds)
- **SSL Verification**: Secure HTTPS connections with certificate validation
- **Rate Limiting**: Respects API rate limits with appropriate delays

## Logging

Configure logging levels for debugging:

```bash
# Enable debug logging
iucn-client get_countries --log-level DEBUG

# Enable info logging
iucn-client get_countries --log-level INFO
```

## Examples

### Research Use Cases

```bash
# Get all endangered species globally
iucn-client get_red_list_categories_code -p code=EN

# Get all marine species assessments
iucn-client get_habitats_code -p code="9"

# Get all mammal assessments
iucn-client get_comprehensive_groups_name -p name=mammals

# Get species declining in population
iucn-client get_population_trends_code -p code=1
```

### Conservation Analysis

```python
from iucn_red_list_client import IUCNRedListClient

client = IUCNRedListClient()

# Analyze threat levels by country
countries = client.call_endpoint('get_countries')
for country in countries:
    endangered = client.call_endpoint('get_countries_code', code=country['code'])
    print(f"{country['description']['en']}: {len(endangered.get('assessments', []))} species assessments")

# Get comprehensive threat analysis
threats = client.call_endpoint('get_threats')
for threat in threats.get('result', []):
    species = client.call_endpoint('get_threats_code', code=threat['code'])
    print(f"Threat '{threat['title']}': affects {len(species.get('assessments', []))} species")
```

## API Reference

### IUCNRedListClient Class

#### Methods

- `__init__(config_file=None, **kwargs)` - Initialize client
- `call_endpoint(endpoint_name, **kwargs)` - Call specific API endpoint

#### Configuration Parameters

- `api_token` (str): IUCN Red List API token
- `base_url` (str): API base URL (default: https://api.iucnredlist.org)

## Project Structure

```
iucn-red-list-client/
├── README.md                           # Main documentation
├── LICENSE                             # CC BY-NC 4.0 license
├── pyproject.toml                      # Package configuration
├── requirements.txt                    # Runtime dependencies
├── .gitignore                          # Git ignore patterns
├── iucn_red_list_client/              # Main package
│   ├── __init__.py                    # Package initialization
│   ├── __version__.py                 # Version information
│   ├── api_client.py                  # Main client code
│   └── api_endpoints.py               # Generated endpoint definitions
├── examples/                          # Example scripts and usage
│   ├── README.md                      # Examples documentation
│   ├── basic_usage.py                 # Basic API usage examples
│   ├── check_species_status.py        # Species conservation checker
│   ├── sample_species.csv             # Sample input data
│   ├── requirements-species-checker.txt # Additional dependencies
│   └── SPECIES_CHECKER_README.md      # Species checker documentation
├── docs/                              # Additional documentation
│   ├── README.md                      # Documentation index
│   ├── INSTALLATION.md                # Installation guide
│   └── CHANGELOG.md                   # Version history
├── config/                            # Configuration templates
│   ├── README.md                      # Configuration guide
│   └── iucn_client.json.example       # Configuration template
├── tests/                             # Test suite
│   ├── README.md                      # Testing documentation
│   ├── run_tests.py                   # Test runner script
│   └── test_*.py                      # Test files
└── tools/                             # Development tools
    ├── README.md                      # Tools documentation
    ├── generate_endpoints.py          # Endpoint generator
    └── openapi.yaml                   # OpenAPI specification
```

## Development

### Running Tests

```bash
# Install development dependencies
pip install -e .[dev]

# Run all tests
pytest

# Run unit tests only (no API access required)
pytest -m unit

# Run integration tests (requires API token)
pytest -m integration

# Run with coverage report
pytest --cov=iucn_red_list_client --cov-report=html
```

### API Endpoint Generation

The API endpoints are automatically generated from the OpenAPI specification:

```bash
# Regenerate endpoints (requires PyYAML)
cd tools
python generate_endpoints.py
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## Troubleshooting

### Common Issues

1. **Authentication Errors**: Ensure your API token is valid and properly set
2. **Rate Limiting**: The API has rate limits; use appropriate delays between requests
3. **Network Timeouts**: Increase timeout values for slow connections
4. **SSL Errors**: Ensure your system has up-to-date SSL certificates

### Debug Mode

Enable debug logging to troubleshoot issues:

```bash
iucn-client get_countries --log-level DEBUG
```

## License

Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) - see [LICENSE](LICENSE) file for details.

## Support

For issues and questions:
- Check the [IUCN Red List API documentation](https://api.iucnredlist.org/api-docs/index.html)
- Review the troubleshooting section above
- Submit issues to the repository issue tracker

## Acknowledgments

- IUCN Red List team for providing the API
- Conservation research community for feedback and testing
