import logging
import os

# Set up logging configuration
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()  # Setting up default to INFO 
log_filename = os.getenv('LOG_FILE', 'app.log')  # Default log file is 'app.log'

logging.basicConfig(
    level=log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()  # This will log to the terminal as well
    ]
)

logger = logging.getLogger(__name__)

