# Development Tools

This directory contains tools for developing and maintaining the IUCN Red List API client.

## Files

### `generate_endpoints.py`
Script to generate API endpoints from the OpenAPI specification.

**Usage:**
```bash
cd tools
python generate_endpoints.py
```

**Requirements:**
- PyYAML (`pip install PyYAML`)

**What it does:**
- Parses `openapi.yaml` 
- Generates `../iucn_red_list_client/api_endpoints.py`
- Creates endpoint definitions with parameters, descriptions, and metadata

### `openapi.yaml`
OpenAPI specification file for the IUCN Red List API v4.

**Source:** Downloaded from the IUCN Red List API documentation
**Purpose:** Used to automatically generate client endpoint definitions
**Format:** OpenAPI 3.0.1 specification

## Regenerating Endpoints

When the IUCN Red List API is updated:

1. Download the latest OpenAPI spec and replace `openapi.yaml`
2. Run the endpoint generator:
   ```bash
   cd tools
   python generate_endpoints.py
   ```
3. Test the updated client to ensure compatibility
4. Update version numbers and documentation as needed

## Development Workflow

1. Make changes to the OpenAPI spec or generator script
2. Regenerate endpoints
3. Test the client functionality
4. Update documentation if new endpoints are added
5. Commit changes including both the tool updates and generated code
