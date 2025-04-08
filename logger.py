import logging
import os

def setup_logger():
    # Get environment variables or fallback to defaults
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()  # Default to INFO
    log_filename = os.getenv('LOG_FILE', 'app.log')  # Default log file is 'app.log'
    
    # Set up logging configuration
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()  # This will log to the terminal as well
        ]
    )

# Initialize logger after setting up configuration
logger = logging.getLogger(__name__)

# Run this function to set up logging when you need it in production
setup_logger()

