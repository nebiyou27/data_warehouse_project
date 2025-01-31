import unittest
from unittest.mock import patch
import logging

from logging_config import log_info, log_error, log_warning, log_debug

class TestLogging(unittest.TestCase):
    
    @patch('logging_config.logging.info')  # Mocking the log_info function
    def test_log_info(self, mock_log_info):
        log_info("Test info message")
        mock_log_info.assert_called_with("Test info message")  # Verifying if log_info was called with the correct message

    @patch('logging_config.logging.error')  # Mocking the log_error function
    def test_log_error(self, mock_log_error):
        log_error("Test error message")
        mock_log_error.assert_called_with("Test error message")  # Verifying if log_error was called with the correct message

    @patch('logging_config.logging.warning')  # Mocking the log_warning function
    def test_log_warning(self, mock_log_warning):
        log_warning("Test warning message")
        mock_log_warning.assert_called_with("Test warning message")  # Verifying if log_warning was called with the correct message

    @patch('logging_config.logging.debug')  # Mocking the log_debug function
    def test_log_debug(self, mock_log_debug):
        log_debug("Test debug message")
        mock_log_debug.assert_called_with("Test debug message")  # Verifying if log_debug was called with the correct message

    @patch('logging_config.logging.error')  # Mocking the log_error function for error case
    def test_log_error_with_exception(self, mock_log_error):
        try:
            raise ValueError("Test Exception")
        except Exception as e:
            log_error(f"Error occurred: {e}")
        mock_log_error.assert_called_with('Error occurred: Test Exception')  # Verifying the error logging

if __name__ == '__main__':
    unittest.main()
