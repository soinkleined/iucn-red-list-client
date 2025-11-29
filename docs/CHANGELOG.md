# Changelog

All notable changes to the IUCN Red List API Client will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-11-23

### Added
- Initial release of IUCN Red List API Client
- Complete support for all IUCN Red List API v4 endpoints
- Command-line interface with comprehensive options
- Python API for programmatic access
- Automatic pagination support with `--all` flag
- Environment variable and JSON configuration support
- Bearer token authentication
- SSL certificate validation with truststore
- Automatic retry logic with exponential backoff
- Structured logging with configurable levels
- Comprehensive error handling
- Built-in help and endpoint listing
- Example scripts for common use cases
- Full documentation and README

### Features
- **49 API endpoints** automatically generated from OpenAPI specification
- **Flexible authentication** via environment variables or config files
- **Robust error handling** with automatic retries and timeout management
- **Pagination support** for handling large datasets
- **CLI and Python API** for different use cases
- **Conservation research tools** with example analysis scripts
- **Cross-platform compatibility** (Windows, macOS, Linux)

### Endpoints Supported
- Assessment data retrieval
- Biogeographical realm assessments
- Comprehensive group data
- Conservation action information
- Country-specific species data
- FAO region assessments
- Growth form classifications
- Green Status assessments
- Habitat-based species data
- API information and versioning
- Population trend analysis
- Red List category data
- Research classification data
- Scope-based assessments
- Statistical information
- Stress factor analysis
- System classifications
- Taxonomic data (kingdom through species)
- Threat assessment data
- Use and trade information

### Configuration Options
- `IUCN_API_TOKEN`: Bearer token for API authentication
- `IUCN_BASE_URL`: Custom API base URL (optional)
- JSON configuration file support
- Command-line parameter overrides

### CLI Features
- `--list-endpoints`: Display all available API endpoints
- `--all`: Automatically paginate through all results
- `--log-level`: Configurable logging (DEBUG, INFO, WARNING, ERROR)
- `--config`: Custom configuration file path
- `-p, --param`: Parameter passing (key=value format)

### Python API Features
- `IUCNRedListClient`: Main client class
- `call_endpoint()`: Single endpoint calls
- `get_all_pages()`: Automatic pagination
- Flexible configuration loading
- Session management with retry logic

### Documentation
- Comprehensive README with usage examples
- Example scripts for research use cases
- Configuration templates
- Troubleshooting guide
- API reference documentation

### Dependencies
- `requests>=2.25.1`: HTTP client library
- `truststore>=0.8.0`: SSL certificate validation
- `PyYAML`: OpenAPI specification parsing (development only)

### Supported Python Versions
- Python 3.8+
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13

### License
- MIT License for open source usage
