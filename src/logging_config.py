import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('scraping.log'),
            logging.StreamHandler()
        ]
    )

def log_error(message):
    logging.error(message)

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_debug(message):
    logging.debug(message)
