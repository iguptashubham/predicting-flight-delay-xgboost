import pandas as pd
from pathlib import Path
from utils.logger import custom_logger

collect_log = custom_logger(file_name='data_collection')

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / 'data' / 'raw'

df = pd.read_csv(r'https://raw.githubusercontent.com/YBI-Foundation/Dataset/refs/heads/main/Airline%20Delay.csv')

save_path = DATA_DIR / 'airline_delay.csv'

collect_log.info(msg = f"data saving into {save_path}")

df.to_csv(save_path,index=False)