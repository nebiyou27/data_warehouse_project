import logging
import pytest
from src.logging_config import setup_logging

def test_setup_logging():
    """Test that the logging setup is correct."""
    # Setup logger using the logging_config
    logger = setup_logging()

    # Assert logger is an instance of logging.Logger
    assert isinstance(logger, logging.Logger), "Logger is not an instance of logging.Logger."

    # Assert logger has at least one handler
    assert len(logger.handlers) > 0, "Logger has no handlers."

    # Assert the logging level is correctly set to INFO (or adjust according to your configuration)
    expected_level = logging.INFO
    actual_level = logger.level
    assert actual_level == expected_level, f"Expected logging level {logging.getLevelName(expected_level)}, but got {logging.getLevelName(actual_level)}."
