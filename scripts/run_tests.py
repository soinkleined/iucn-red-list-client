#!/usr/bin/env python3
"""
Test runner script for IUCN Red List API Client.

This script provides convenient commands for running different types of tests.
"""

import sys
import subprocess
import argparse


def run_command(cmd):
    """Run a command and return the result."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    
    return result.returncode


def main():
    """Main test runner function."""
    parser = argparse.ArgumentParser(description='Run tests for IUCN Red List API Client')
    parser.add_argument(
        'test_type',
        choices=['unit', 'integration', 'all', 'coverage'],
        help='Type of tests to run'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    base_cmd = ['python', '-m', 'pytest']
    
    if args.verbose:
        base_cmd.append('-v')
    
    if args.test_type == 'unit':
        cmd = base_cmd + ['-m', 'unit']
    elif args.test_type == 'integration':
        cmd = base_cmd + ['-m', 'integration']
    elif args.test_type == 'coverage':
        cmd = base_cmd + ['--cov=iucn_red_list_client', '--cov-report=html', '--cov-report=term']
    else:  # all
        cmd = base_cmd
    
    return run_command(cmd)


if __name__ == '__main__':
    sys.exit(main())
