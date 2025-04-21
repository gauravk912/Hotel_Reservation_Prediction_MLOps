import logging
import os 
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True) #if already exists, do nothing otherwise create it

LOG_FILE = os.path.join(LOGS_DIR,f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename = LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level = logging.INFO
)
#There are maily 3 levels for logging  Info, Warning, Error
#level --> .info means only info , warning and error will be shown as only warning and error are above info

def get_logger(name):
    """
    Function to get a logger with the specified name.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger