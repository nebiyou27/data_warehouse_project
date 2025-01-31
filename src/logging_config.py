import logging
import os
from pathlib import Path

def setup_logging(log_dir="logs"):
    """
    Set up logging configuration
    
    Args:
        log_dir (str): Directory where log files will be stored. Defaults to 'logs'
    
    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    Path(log_dir).mkdir(exist_ok=True)
    
    # Create logger
    logger = logging.getLogger('telegram_scraper')
    logger.setLevel(logging.INFO)
    
    # Create handlers
    file_handler = logging.FileHandler(
        os.path.join(log_dir, 'scraping.log')
    )
    console_handler = logging.StreamHandler()
    
    # Create formatters and add it to handlers
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger