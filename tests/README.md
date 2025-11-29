# Tests

This directory contains the test suite for the IUCN Red List API Client.

## Test Structure

### Unit Tests (`@pytest.mark.unit`)
- `test_api_client.py` - Tests for the main API client class
- `test_cli.py` - Tests for the command-line interface
- `test_endpoints.py` - Tests for API endpoint configuration
- `test_species_checker.py` - Tests for the species conservation checker

### Integration Tests (`@pytest.mark.integration`)
- `test_integration.py` - Tests requiring actual API access

## Running Tests

### Install Test Dependencies
```bash
pip install -e .[dev]
```

### Run All Tests
```bash
pytest
```

### Run Specific Test Types
```bash
# Unit tests only (no API access required)
pytest -m unit

# Integration tests only (requires API token)
pytest -m integration

# Run with coverage
pytest --cov=iucn_red_list_client --cov-report=html
```

### Using the Test Runner
```bash
# Run unit tests
python run_tests.py unit

# Run integration tests
python run_tests.py integration

# Run all tests
python run_tests.py all

# Run with coverage report
python run_tests.py coverage
```

## Test Configuration

### Environment Variables
For integration tests, set:
```bash
export IUCN_API_TOKEN="your_api_token_here"
```

### Test Markers
- `@pytest.mark.unit` - Unit tests (fast, no external dependencies)
- `@pytest.mark.integration` - Integration tests (require API access)
- `@pytest.mark.slow` - Slow running tests

### Configuration Files
- `pytest.ini` - Pytest configuration
- `conftest.py` - Test fixtures and utilities

## Test Coverage

The test suite covers:
- ✅ Client initialization and configuration
- ✅ API request handling and error cases
- ✅ Endpoint calling with parameters
- ✅ CLI argument parsing and execution
- ✅ Species checker functionality
- ✅ API endpoint structure validation
- ✅ Integration with real API (when token provided)

## Writing New Tests

### Unit Test Example
```python
@pytest.mark.unit
def test_my_function():
    """Test description."""
    result = my_function("input")
    assert result == "expected"
```

### Integration Test Example
```python
@pytest.mark.integration
def test_api_call(self):
    """Test actual API call."""
    if not os.getenv('IUCN_API_TOKEN'):
        pytest.skip("API token not available")
    
    client = IUCNRedListClient()
    result = client.call_endpoint('get_countries')
    assert result is not None
```

## Continuous Integration

Tests are designed to run in CI environments:
- Unit tests run without external dependencies
- Integration tests are skipped if API token is not available
- Coverage reports can be generated for code quality metrics
