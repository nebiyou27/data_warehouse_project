import logging
import os

# Configuration (Best Practice: Use environment variables for flexibility)
LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG").upper()  # Default to DEBUG
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Create a logger (Do this ONCE per module)
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL) # Set log level based on env variable

# Add a handler (StreamHandler for console output)
handler = logging.StreamHandler()  # Or FileHandler(...) for file output
formatter = logging.Formatter(LOG_FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)


def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)

def log_warning(message):
    logger.warning(message)

def log_debug(message):
    logger.debug(message)

# Example usage (only when running this file directly, not during tests)
if __name__ == "__main__":
    log_info("This is an info message from logging_config")
    log_error("This is an error message from logging_config")
    log_warning("This is a warning message from logging_config")
    log_debug("This is a debug message from logging_config")