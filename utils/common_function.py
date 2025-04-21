import os
import pandas as pd
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml
import sys

logger = get_logger(__name__)

#
def read_yaml(yaml_file_path):
    """
    Function to read a YAML file and return its contents.
    """
    try:
        with open(yaml_file_path, 'r') as file:
            config = yaml.safe_load(file)
        logger.info(f"YAML file {yaml_file_path} loaded successfully.")
        return config
    except Exception as e:
        logger.error(f"Error reading YAML file {yaml_file_path}: {e}")
        raise CustomException(f"Error reading YAML file: {e}", sys) from e
    
def load_data(path):
    try:
        logger.info("Loading data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"Error loading the data {e}")
        raise CustomException("Failed to load data" , e)