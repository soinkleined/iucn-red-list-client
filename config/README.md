# Configuration

This directory contains configuration file templates and examples.

## Files

### `iucn_client.json.example`
Example configuration file template.

**Usage:**
```bash
# Copy to your preferred location
cp config/iucn_client.json.example ~/.iucn_client.json

# Edit with your credentials
nano ~/.iucn_client.json
```

**Configuration options:**
- `api_token`: Your IUCN Red List API token (required)
- `base_url`: API base URL (optional, defaults to https://api.iucnredlist.org)

## Configuration Methods

### 1. Environment Variables (Recommended)
```bash
export IUCN_API_TOKEN="your_api_token_here"
export IUCN_BASE_URL="https://api.iucnredlist.org"  # Optional
```

### 2. Default Config File
Place configuration at `~/.iucn_client.json`

### 3. Custom Config File
```bash
iucn-client --config /path/to/config.json get_countries
```

## Getting an API Token

1. Visit https://api.iucnredlist.org/api/v4/docs
2. Register for an account
3. Generate an API token
4. Use the token in your configuration

## Security Notes

- Never commit configuration files with real API tokens to version control
- Use environment variables in production environments
- Keep your API token secure and don't share it publicly
