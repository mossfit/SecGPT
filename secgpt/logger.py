import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name, verbose=False):
    """
    Return a logger instance with a rotating file handler and console output.
    
    Args:
        name (str): Name of the logger.
        verbose (bool): If True, set log level to DEBUG, otherwise INFO.
        
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    # Avoid adding handlers multiple times if logger is already configured.
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    
    # Formatter for log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File Handler with rotation
    if not os.path.exists("logs"):
        os.makedirs("logs")
    file_handler = RotatingFileHandler("logs/secgpt.log", maxBytes=5*1024*1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
