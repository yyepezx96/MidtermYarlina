import logging

logger = logging.getLogger(__name__)

def add(a, b):
    logger.info(f"Adding {a} and {b}")
    try:
        result = a + b
        logger.info(f"Result of addition: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in add function: {e}")
        raise

def subtract(a, b):
    logger.info(f"Subtracting {b} from {a}")
    try:
        result = a - b
        logger.info(f"Result of subtraction: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in subtract function: {e}")
        raise

def multiply(a, b):
    logger.info(f"Multiplying {a} and {b}")
    try:
        result = a * b
        logger.info(f"Result of multiplication: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in multiply function: {e}")
        raise

def divide(a, b):
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

