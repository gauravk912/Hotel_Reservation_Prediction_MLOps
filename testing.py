from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger = get_logger(__name__)

def divide_number(a,b):
    try:
        result = a/b
        logger.info("dividing 2 numbers")
        return result
    except Exception as e:
        logger.error("Error occurred")
        raise CustomException("0 error",sys)
    
if __name__ == "__main__":
    try:
        result = divide_number(10,0)
        print(f"Result: {result}")
    except CustomException as e:
        logger.error(e)