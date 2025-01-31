import logging
import pytest
from ..src.logging_config import setup_logging

def test_setup_logging():
    """Test that logging is set up correctly."""
    logger = setup_logging()

    # Ensure logger is an instance of logging.Logger
    assert isinstance(logger, logging.Logger)

    # Ensure logger has handlers
    assert len(logger.handlers) > 0

    # Ensure logging level is set correctly
    assert logger.level == logging.INFO  # Update to match your actual logging level.
