"""
Tests for the hello_world module.
"""

import io
import sys
from unittest.mock import patch

from main import hello_world, main


class TestHelloWorld:
    """Test cases for the hello_world function."""

    def test_hello_world_default(self):
        """Test hello_world with default argument."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            hello_world()
            assert mock_stdout.getvalue() == "Hello, World!\n"

    def test_hello_world_custom_name(self):
        """Test hello_world with custom name argument."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            hello_world("Alice")
            assert mock_stdout.getvalue() == "Hello, Alice!\n"

    def test_hello_world_empty_string(self):
        """Test hello_world with empty string name."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            hello_world("")
            assert mock_stdout.getvalue() == "Hello, !\n"

    def test_hello_world_special_characters(self):
        """Test hello_world with special characters in name."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            hello_world("测试")
            assert mock_stdout.getvalue() == "Hello, 测试!\n"

    def test_hello_world_with_numbers(self):
        """Test hello_world with numbers in name."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            hello_world("User123")
            assert mock_stdout.getvalue() == "Hello, User123!\n"


class TestMain:
    """Test cases for the main function."""

    def test_main_output(self):
        """Test main function produces correct output."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            assert mock_stdout.getvalue() == "Hello, World!\n"
