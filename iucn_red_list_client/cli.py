"""
CLI interface for IUCN Red List API Client.
"""

import argparse
import json
import logging
import sys
import textwrap

from .api_endpoints import API_ENDPOINTS
from .client import IUCNRedListClient

# Logger setup
logger = logging.getLogger(__name__)


def show_endpoint_help(endpoint_name: str) -> None:
    """Display help information for a specific endpoint."""
    endpoint_info = API_ENDPOINTS.get(endpoint_name)
    if endpoint_info:
        print(f'{endpoint_name}:\n')
        print(f"{', '.join(endpoint_info['tags'])}\n")
        print(f"{endpoint_info['summary']}\n")
        endpoint_description = textwrap.fill(endpoint_info['description'], 72)
        print(f'{endpoint_description}\n')
        
        # Show path parameters
        if endpoint_info['path_params']:
            print("Path Parameters:")
            for param in endpoint_info['path_params']:
                print(f"Parameter        : {param}")
                print(f"  Location       : path")
                print(f"  Required       : Yes")
                print(f"  Type           : string")
                print()
        
        # Show query parameters
        if endpoint_info['query_params']:
            print("Query Parameters:")
            for param in endpoint_info['query_params']:
                param_description = f"Query parameter for {endpoint_name}"
                param_description = textwrap.fill(param_description, 53, subsequent_indent=" " * 19)
                print(f"Parameter        : {param['name']}")
                print(f"  Description    : {param_description}")
                print(f"  Location       : query")
                print(f"  Required       : {'Yes' if param['required'] else 'No'}")
                print(f"  Type           : {param['type']}")
                print()
        
        print(f"Authentication   : {'Required' if endpoint_info['requires_auth'] else 'Not Required'}")
        print(f"HTTP Method      : {endpoint_info['method']}")
        print(f"API Path         : {endpoint_info['path']}")
    else:
        logger.error(f"Endpoint '{endpoint_name}' not found.")


def create_argument_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    def formatter(prog: str) -> argparse.HelpFormatter:
        """Format help output with wider display."""
        return argparse.HelpFormatter(prog, max_help_position=100, width=200)

    parser = argparse.ArgumentParser(
        description='A CLI for accessing the IUCN Red List API v4.',
        formatter_class=formatter
    )

    parser.add_argument(
        'endpoint',
        nargs='?',
        type=str,
        help='The endpoint name from the API (e.g., get_taxa_scientific_name).'
    )
    parser.add_argument(
        'parameters',
        nargs='*',
        help='Positional parameters for the endpoint. Use "help" to display more information about the endpoint.'
    )
    parser.add_argument(
        '--config',
        help='Configuration file path'
    )
    parser.add_argument(
        '--list-endpoints',
        action='store_true',
        help='List available endpoints'
    )
    parser.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        default='WARNING',
        help='Set logging level (default: WARNING).'
    )
    parser.add_argument(
        '-p', '--param',
        action='append',
        help='Parameters in key=value format. You can specify multiple parameters.'
    )

    return parser


def main() -> None:
    """CLI entry point."""
    
    # Store original argv
    original_argv = sys.argv[:]
    
    # Check for endpoint-specific help before argparse processes arguments
    if len(original_argv) >= 3 and ('help' in original_argv):
        endpoint_name = None
        for arg in original_argv[1:]:
            if not arg.startswith('-') and arg != original_argv[0] and arg != 'help':
                endpoint_name = arg
                break
        
        if endpoint_name and endpoint_name in API_ENDPOINTS:
            show_endpoint_help(endpoint_name)
            return
    
    # Filter out 'help' argument for argparse
    filtered_argv = [arg for arg in original_argv if arg != 'help']
    
    parser = create_argument_parser()
    args = parser.parse_args(filtered_argv[1:])
    
    # Set up logging
    logging.basicConfig(
        level=getattr(logging, args.log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    if args.list_endpoints:
        print("Available endpoints:")
        for name, info in API_ENDPOINTS.items():
            method = info.get('method', 'unknown').upper()
            summary = info.get('summary', 'No summary')
            print(f"  {name} ({method}) - {summary}")
        return
    
    if not args.endpoint:
        parser.print_help()
        return
    
    # Check if help was requested via parameters
    if args.parameters and args.parameters[0].lower() == 'help':
        show_endpoint_help(args.endpoint)
        return
    
    # Parse parameters
    params = {}
    if args.param:
        for param in args.param:
            if '=' in param:
                key, value = param.split('=', 1)
                params[key] = value
    
    # Create client and make request
    client = IUCNRedListClient(config_file=args.config)
    
    try:
        result = client.call_endpoint(args.endpoint, **params)
        print(json.dumps(result, indent=2))
        
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
