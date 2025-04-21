import os

## Data Ingestion
RAW_DIR = "artifacts/raw"
RAW_FILE_PATH = os.path.join(RAW_DIR, "raw_data.csv")
TRAIN_FILE_PATH = os.path.join(RAW_DIR, "train_data.csv")
TEST_FILE_PATH = os.path.join(RAW_DIR, "test_data.csv")

CONFIG_PATH = "config/config.yaml"


############################# DATA PROCESSING #############################

PROCESSED_DIR = "artifacts/processed"
PROCESSED_TRAIN_DATA_PATH = os.path.join(PROCESSED_DIR, "processed_train_data.csv")
PROCESSED_TEST_DATA_PATH = os.path.join(PROCESSED_DIR, "processed_test_data.csv")
PROCESSED_MODEL_DIR = "artifacts/model"


############################ MODEL TRAINING #############################
MODEL_OUTPUT_PATH= "artifacts/models/lgbm_model.pkl"
