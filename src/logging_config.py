import logging
import os

# Ensure logs directory exists
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Set up logging configuration
def setup_logging():
    log_file = os.path.join(LOG_DIR, "scraping.log")
    error_log_file = os.path.join(LOG_DIR, "error.log")

    # Configure the logger
    logging.basicConfig(
        level=logging.INFO,  # Ensure INFO level is set
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.FileHandler(error_log_file),
            logging.StreamHandler()  # Output logs to console as well
        ]
    )

    # Create logger
    logger = logging.getLogger()
    
    # Explicitly set the logging level to INFO in case it's inherited wrongly
    logger.setLevel(logging.INFO)

    return logger
