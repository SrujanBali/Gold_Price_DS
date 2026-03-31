import pandas as pd
from gold_price_ds.config import RAW_DATA_DIR, PROCESSED_DATA_DIR

def load_raw_data(filename = "gold_price_forecasting_dataset.csv"):
    #Load dataset.csv and does basic time series sorting and cleaning
    file_path = RAW_DATA_DIR / filename

    data = pd.read_csv(file_path, index_col="date")
    data.index = pd.to_datetime(data.index)
    data.sort_index(inplace=True)

    return data

def load_processed_data(filename = "gold_price_processed_log.csv"):
    #Load the processed dataset after the first notebook
    filepath = PROCESSED_DATA_DIR / filename

    data = pd.read_csv(filepath, index_col='date')
    data.index = pd.to_datetime(data.index)
    data.sort_index(inplace=True)

    return data