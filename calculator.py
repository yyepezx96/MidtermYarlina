import logging

# Create a logger for the module
logger = logging.getLogger(__name__)

def check_valid_input(a, b):
    """
    Check if both arguments are numbers (int or float).
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers.")

def add(a, b):
    """
    Adds two numbers together and logs the result.
    """
    check_valid_input(a, b)  # Ensure inputs are valid
    logger.info(f"Adding {a} and {b}")
    try:
        result = a + b
        logger.info(f"Result of addition: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in add function: {e}")
        raise

def subtract(a, b):
    """
    Subtracts the second number from the first and logs the result.
    """
    check_valid_input(a, b)  # Ensure inputs are valid
    logger.info(f"Subtracting {b} from {a}")
    try:
        result = a - b
        logger.info(f"Result of subtraction: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in subtract function: {e}")
        raise

def multiply(a, b):
    """
    Multiplies two numbers together and logs the result.
    """
    check_valid_input(a, b)  # Ensure inputs are valid
    logger.info(f"Multiplying {a} and {b}")
    try:
        result = a * b
        logger.info(f"Result of multiplication: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in multiply function: {e}")
        raise

def divide(a, b):
    """
    Divides the first number by the second and logs the result.
    Handles division by zero.
    """
    check_valid_input(a, b)  # Ensure inputs are valid
    logger.info(f"Dividing {a} by {b}")
    try:
        if b == 0:
            logger.warning("Attempted division by zero!")
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        logger.info(f"Result of division: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in divide function: {e}")
        raise

