"""
IUCN Red List API Client - A Python client for the IUCN Red List API v4

Environment Variable Priority:
1. If ANY IUCN_* environment variables are set, ALL required ones must be present
2. Environment variables completely bypass config files
3. Falls back to config file only if NO environment variables are detected

Supported IUCN_* Environment Variables:
- IUCN_API_TOKEN (required): Bearer token for API authentication
- IUCN_BASE_URL (optional): Base URL for the API (defaults to https://api.iucnredlist.org)
"""

import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, Optional, TypedDict

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import truststore
truststore.inject_into_ssl()

from .api_endpoints import API_ENDPOINTS

# Constants
REQUEST_TIMEOUT = 30
DEFAULT_BASE_URL = "https://api.iucnredlist.org"

# Logger setup
logger = logging.getLogger(__name__)

class EnvConfig(TypedDict, total=False):
    """Type definition for environment variable configuration."""
    api_token: str
    base_url: str

class IUCNRedListClient:
    """IUCN Red List API Client."""
    
    def __init__(self, config_file: Optional[str] = None, **kwargs):
        """Initialize the client."""
        self.session = requests.Session()
        self._setup_retry_strategy()
        
        # Load configuration
        self.config = self._load_config(config_file, **kwargs)
        
        # Set up authentication
        if self.config.get('api_token'):
            self.session.headers.update({
                'Authorization': self.config['api_token']
            })
        
        self.base_url = self.config.get('base_url', DEFAULT_BASE_URL)
        
    def _setup_retry_strategy(self) -> None:
        """Set up retry strategy for requests."""
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
    
    def _load_config(self, config_file: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """Load configuration from environment variables or config file."""
        
        # Check for environment variables first
        env_config = self._load_env_config()
        if env_config:
            logger.info("Using environment variable configuration")
            return env_config
        
        # Override with any kwargs
        if kwargs:
            logger.info("Using provided configuration parameters")
            return kwargs
            
        # Fall back to config file
        if config_file and Path(config_file).exists():
            logger.info(f"Loading configuration from {config_file}")
            with open(config_file, 'r') as f:
                return json.load(f)
        
        # Try default config file
        default_config = Path.home() / '.iucn_client.json'
        if default_config.exists():
            logger.info(f"Loading configuration from {default_config}")
            with open(default_config, 'r') as f:
                return json.load(f)
        
        logger.warning("No configuration found. API token required for authenticated endpoints.")
        return {}
    
    def _load_env_config(self) -> Optional[EnvConfig]:
        """Load configuration from environment variables."""
        env_vars = {k: v for k, v in os.environ.items() if k.startswith('IUCN_')}
        
        if not env_vars:
            return None
        
        config = {}
        
        # Required variables
        if 'IUCN_API_TOKEN' in env_vars:
            config['api_token'] = env_vars['IUCN_API_TOKEN']
        
        # Optional variables
        if 'IUCN_BASE_URL' in env_vars:
            config['base_url'] = env_vars['IUCN_BASE_URL']
        
        return config
    
    def _make_request(self, method: str, path: str, **kwargs) -> requests.Response:
        """Make HTTP request to API."""
        url = f"{self.base_url.rstrip('/')}{path}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=REQUEST_TIMEOUT,
                **kwargs
            )
            response.raise_for_status()
            return response
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise
    
    def call_endpoint(self, endpoint_name: str, **kwargs) -> Dict[str, Any]:
        """Call a specific API endpoint."""
        if endpoint_name not in API_ENDPOINTS:
            raise ValueError(f"Unknown endpoint: {endpoint_name}")
        
        endpoint_info = API_ENDPOINTS[endpoint_name]
        path = endpoint_info['path']
        method = endpoint_info['method']
        
        # Handle path parameters
        path_params = {}
        for param_name in endpoint_info.get('path_params', []):
            if param_name in kwargs:
                path_params[param_name] = kwargs.pop(param_name)
            else:
                raise ValueError(f"Missing required path parameter: {param_name}")
        
        # Format path with parameters
        if path_params:
            path = path.format(**path_params)
        
        # Handle query parameters
        query_params = {}
        for param_info in endpoint_info.get('query_params', []):
            param_name = param_info['name']
            if param_name in kwargs:
                query_params[param_name] = kwargs.pop(param_name)
            elif param_info.get('required', False):
                raise ValueError(f"Missing required query parameter: {param_name}")
        
        # Make the request
        request_kwargs = {}
        if query_params:
            request_kwargs['params'] = query_params
        
        response = self._make_request(method, path, **request_kwargs)
        return response.json()
