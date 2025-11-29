"""Tests for the CLI interface."""

import pytest
import sys
from unittest.mock import patch, Mock
from iucn_red_list_client.api_client import main, create_argument_parser


class TestCLI:
    """Test cases for CLI functionality."""

    @pytest.mark.unit
    def test_argument_parser_creation(self):
        """Test argument parser creation."""
        parser = create_argument_parser()
        assert parser is not None
        
        # Test parsing basic arguments
        args = parser.parse_args(['get_countries'])
        assert args.endpoint == 'get_countries'

    @pytest.mark.unit
    def test_argument_parser_with_params(self):
        """Test argument parser with parameters."""
        parser = create_argument_parser()
        args = parser.parse_args(['get_countries_code', '-p', 'code=US'])
        
        assert args.endpoint == 'get_countries_code'
        assert args.param == ['code=US']

    @pytest.mark.unit
    def test_argument_parser_list_endpoints(self):
        """Test argument parser with list endpoints flag."""
        parser = create_argument_parser()
        args = parser.parse_args(['--list-endpoints'])
        
        assert args.list_endpoints is True

    @pytest.mark.unit
    @patch('sys.argv', ['iucn-client', '--list-endpoints'])
    def test_main_list_endpoints(self, capsys):
        """Test main function with list endpoints."""
        main()
        captured = capsys.readouterr()
        assert 'Available endpoints:' in captured.out
        assert 'get_countries' in captured.out

    @pytest.mark.unit
    @patch('sys.argv', ['iucn-client', 'get_countries', 'help'])
    def test_main_endpoint_help(self, capsys):
        """Test main function with endpoint help."""
        main()
        captured = capsys.readouterr()
        assert 'get_countries:' in captured.out

    @pytest.mark.unit
    @patch('sys.argv', ['iucn-client'])
    def test_main_no_endpoint(self, capsys):
        """Test main function with no endpoint."""
        main()
        captured = capsys.readouterr()
        assert 'usage:' in captured.out

    @pytest.mark.unit
    @patch('sys.argv', ['iucn-client', 'get_countries'])
    @patch('iucn_red_list_client.api_client.IUCNRedListClient')
    def test_main_successful_call(self, mock_client_class, capsys):
        """Test main function with successful API call."""
        # Mock the client instance
        mock_client = Mock()
        mock_client.call_endpoint.return_value = {"test": "data"}
        mock_client_class.return_value = mock_client
        
        main()
        captured = capsys.readouterr()
        assert '"test": "data"' in captured.out

    @pytest.mark.unit
    @patch('sys.argv', ['iucn-client', 'get_countries'])
    @patch('iucn_red_list_client.api_client.IUCNRedListClient')
    def test_main_api_error(self, mock_client_class, capsys):
        """Test main function with API error."""
        # Mock the client to raise an exception
        mock_client = Mock()
        mock_client.call_endpoint.side_effect = Exception("API Error")
        mock_client_class.return_value = mock_client
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        assert exc_info.value.code == 1

    @pytest.mark.unit
    @patch('sys.argv', ['iucn-client', 'get_countries_code', '-p', 'code=US'])
    @patch('iucn_red_list_client.api_client.IUCNRedListClient')
    def test_main_with_parameters(self, mock_client_class, capsys):
        """Test main function with parameters."""
        mock_client = Mock()
        mock_client.call_endpoint.return_value = {"country": "US"}
        mock_client_class.return_value = mock_client
        
        main()
        
        # Verify the endpoint was called with correct parameters
        mock_client.call_endpoint.assert_called_once_with('get_countries_code', code='US')

    @pytest.mark.unit
    @patch('sys.argv', ['iucn-client', 'get_countries', '--log-level', 'DEBUG'])
    @patch('iucn_red_list_client.api_client.IUCNRedListClient')
    def test_main_with_log_level(self, mock_client_class):
        """Test main function with custom log level."""
        mock_client = Mock()
        mock_client.call_endpoint.return_value = {"test": "data"}
        mock_client_class.return_value = mock_client
        
        main()
        
        # Test passes if no exception is raised during logging setup
