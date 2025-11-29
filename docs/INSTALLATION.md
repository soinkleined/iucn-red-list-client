# Installation Guide

## Quick Installation

### From GitHub (Recommended)

```bash
pip install git+https://github.com/soinkleined/iucn-red-list-client.git
```

### From Source

```bash
# Clone the repository
git clone https://github.com/soinkleined/iucn-red-list-client.git
cd iucn-red-list-client

# Install the package
pip install .

# Or install in development mode
pip install -e .
```

### Verify Installation

```bash
# Test CLI
iucn-client --help

# Test Python import
python -c "from iucn_red_list_client import IUCNRedListClient; print('Success!')"

# List available endpoints
iucn-client --list-endpoints
```

## Configuration

### Method 1: Environment Variables (Recommended)

```bash
export IUCN_API_TOKEN="your_api_token_here"
export IUCN_BASE_URL="https://apiv3.iucnredlist.org"  # Optional
```

### Method 2: Configuration File

Create `~/.iucn_client.json`:
```json
{
    "api_token": "your_api_token_here",
    "base_url": "https://apiv3.iucnredlist.org"
}
```

### Method 3: Custom Config File

```bash
# Copy example config
cp iucn_client.json.example my_config.json

# Edit with your credentials
# Then use with --config flag
iucn-client --config my_config.json get_countries
```

## Getting an API Token

1. Visit [IUCN Red List API](https://apiv3.iucnredlist.org/api/v3/docs)
2. Register for an account
3. Generate an API token
4. Use the token in your configuration

## Requirements

- Python 3.8 or higher
- Internet connection for API access
- Valid IUCN Red List API token

## Dependencies

The package automatically installs:
- `requests>=2.25.1` - HTTP client
- `truststore>=0.8.0` - SSL certificate validation

## Development Installation

For development work:

```bash
# Clone repository
git clone https://github.com/soinkleined/iucn-red-list-client.git
cd iucn-red-list-client

# Install development dependencies
pip install -r requirements-dev.txt

# Install package in editable mode
pip install -e .

# Run example scripts
python examples/basic_usage.py
```

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure the package is installed
   ```bash
   pip list | grep iucn
   ```

2. **Authentication Error**: Check your API token
   ```bash
   echo $IUCN_API_TOKEN
   ```

3. **SSL Errors**: Update certificates
   ```bash
   pip install --upgrade certifi truststore
   ```

4. **Permission Errors**: Use virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install .
   ```

### Testing Installation

```bash
# Test without authentication (should work)
iucn-client --list-endpoints

# Test with authentication (requires API token)
iucn-client get_information_api_version
```

## Uninstallation

```bash
pip uninstall iucn-red-list-client
```

## Platform Support

- ✅ macOS
- ✅ Linux
- ✅ Windows
- ✅ Docker containers
- ✅ CI/CD environments
