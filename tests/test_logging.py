import unittest
from unittest.mock import patch
from logging_config import log_info, log_error, log_warning, log_debug

class TestLogging(unittest.TestCase):

    @patch('logging_config.logger.info')
    def test_log_info(self, mock_log_info):
        log_info("Test info message")
        mock_log_info.assert_called_once_with("Test info message")

    @patch('logging_config.logger.error')
    def test_log_error(self, mock_log_error):
        log_error("Test error message")
        mock_log_error.assert_called_once_with("Test error message")

    @patch('logging_config.logger.warning')
    def test_log_warning(self, mock_log_warning):
        log_warning("Test warning message")
        mock_log_warning.assert_called_once_with("Test warning message")

    @patch('logging_config.logger.debug')
    def test_log_debug(self, mock_log_debug):
        log_debug("Test debug message")
        mock_log_debug.assert_called_once_with("Test debug message")

    @patch('logging_config.logger.error')
    def test_log_error_with_exception(self, mock_log_error):
        try:
            raise ValueError("Test Exception")
        except ValueError as e:
            log_error(f"Error occurred: {e}")
        mock_log_error.assert_called_once_with("Error occurred: Test Exception")

if __name__ == '__main__':
    unittest.main()