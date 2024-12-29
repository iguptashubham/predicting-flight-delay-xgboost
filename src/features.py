from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from utils.load_yaml import yaml_loader
from utils.logger import custom_logger

#custom logger to log
data_logger = custom_logger('processing_n_split')

#Root dir of project
ROOT_DIR = Path(__file__).resolve().parent.parent

#data directory
DATA_DIR = ROOT_DIR / 'data'

#feature parameter from params.yaml
feature_param = yaml_loader()['feature']

data_logger.info('Getting paramter from params.yaml')

def processing_n_split(df_path,save_path):
    
    """ 
    This function read the raw data and extract 
    important feature.
    
    split it in train and test
    on feature paramter from
            params.yaml 
    and save into 
            data/processed.
    """
    
    raw_df = pd.read_csv(df_path)
    
    data_logger.info(f'Selecting Important feature from raw data {df_path}')
    
    select_feature = ['carrier','airport','arr_flights', 'arr_del15', 'carrier_ct', 'weather_ct', 'nas_ct',
       'security_ct', 'late_aircraft_ct', 'arr_cancelled', 'arr_diverted',
       'arr_delay', 'carrier_delay', 'weather_delay', 'nas_delay',
       'security_delay', 'late_aircraft_delay']
    
    newdf = raw_df[select_feature].dropna()
    
    data_logger.info(f"Spliting data into test and test dataset and saving in {save_path}")
    
    train_df, test_df = train_test_split(newdf,
                                         test_size=feature_param['test_size'],
                                         shuffle=feature_param['shuffle'])
    
    train_df.to_csv(save_path / 'train.csv',index=False)
    test_df.to_csv(save_path / 'test.csv', index=False)
    
if __name__ == "__main__":
    rawdf = DATA_DIR / 'raw' / 'airline_delay.csv'
    save_path = DATA_DIR / 'processed'
    save_path.mkdir(parents=True, exist_ok=True)
    processing_n_split(df_path=rawdf, save_path=save_path)