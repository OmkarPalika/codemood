"""
Tests for CLI functionality.
"""

import pytest
from unittest.mock import patch, mock_open, MagicMock
from codemood.cli import get_current_version, get_latest_version, main
from io import StringIO

def test_get_current_version():
    """Test getting current version."""
    version = get_current_version()
    assert isinstance(version, str)
    assert len(version) > 0


@patch('requests.get')
def test_get_latest_version_success(mock_get: MagicMock) -> None:
    """Test getting latest version from PyPI."""
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"info": {"version": "0.2.1"}}
    
    version = get_latest_version()
    assert version == "0.2.1"


@patch('requests.get')
def test_get_latest_version_failure(mock_get: MagicMock) -> None:
    """Test handling network failure."""
    mock_get.side_effect = Exception("Network error")
    
    version = get_latest_version()
    assert version is None


@patch('sys.argv', ['codemood', '--version'])
@patch('sys.stdout', new_callable=StringIO)
def test_version_command(mock_stdout: StringIO) -> None:
    """Test version command."""
    with pytest.raises(SystemExit):
        main()
    
    output = mock_stdout.getvalue()
    assert "0.2.0" in output or len(output.strip()) > 0


@patch('builtins.open', new_callable=mock_open, read_data='def hello(): pass')
@patch('sys.argv', ['codemood', '--analyze', 'test.py'])
@patch('sys.stdout', new_callable=StringIO)
def test_analyze_command(mock_stdout: StringIO, mock_file: MagicMock) -> None:
    """Test analyze command."""
    with pytest.raises(SystemExit):
        main()
    
    output = mock_stdout.getvalue()
    assert "Analysis for:" in output or "Overall Score:" in output
