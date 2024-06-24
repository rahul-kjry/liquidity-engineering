import logging

def setup_logging(log_file):
    """Set up logging configuration."""
    logging.basicConfig(filename=log_file, level=logging.INFO)

def log_info(message):
    """Log info message."""
    logging.info(message)

def log_error(message):
    """Log error message."""
    logging.error(message)
