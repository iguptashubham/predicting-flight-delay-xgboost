import json,pickle
import mlflow, mlflow.sklearn, mlflow.xgboost
import pandas as pd
from pathlib import Path
from sklearn.metrics import mean_absolute_error,r2_score,root_mean_squared_error,median_absolute_error, mean_squared_error,mean_squared_log_error
from utils.logger import custom_logger
from utils.load_yaml import yaml_loader
from build_model import xgbmodel_build

ROOT_DIR = Path(__file__).resolve().parent.parent

model_param = yaml_loader()['model_parameter']
train_logger = custom_logger(file_name='train')

def model_training(train_path,test_path,param):
    
    train_logger.info('Splitting test and train data into x and y')
    
    train_df = pd.read_csv(train_path)
    x_train,y_train = train_df.drop('late_aircraft_delay', axis=1), train_df['late_aircraft_delay']
    
    test_df = pd.read_csv(test_path)
    x_test,y_test = test_df.drop('late_aircraft_delay', axis=1), test_df['late_aircraft_delay']
    
    train_logger.info("getting model parameter from params.yaml and addingto model")
    xgbmodel = xgbmodel_build(params=param)
    train_logger.info('Fitting xgboost model on x_train and y_train')
    xgbmodel.fit(x_train,y_train)
    
    pred = xgbmodel.predict(x_test)
    
    metrics = {
        'root_mean_squared_error':root_mean_squared_error(y_test,pred),
        'mean_squared_error':mean_squared_error(y_test,pred),
        'mean_squared_log_error':mean_squared_log_error(y_test,pred),
        'r2_score':r2_score(y_test,pred),
        'mean_absolute_error':mean_absolute_error(y_test,pred),
    }
    
    metrics_path = ROOT_DIR / 'reports' / 'metrics.json'
    
    with open(metrics_path,'w') as json_metrics:
        json.dump(metrics,json_metrics)
    train_logger.info(f'Model metrics saved in {metrics_path} as json')
    
    model_path = ROOT_DIR/'models'/'model.pkl'
    with open(model_path,'wb') as file:
        pickle.dump(xgbmodel,file)
    
    train_logger.info(f'Model saved in {model_path} as pickle')    
   # xgboost_model = xgbmodel.named_steps['XGBRFRegressor']
    #mlflow
    mlrun = ROOT_DIR/'mlruns'
    train_logger.info(f'Experiment tracking by Mlfow in {mlrun} directory') 
    mlflow.set_tracking_uri(mlrun)
    mlflow.set_experiment('Flight Delay Prediction')
    with mlflow.start_run():
        mlflow.log_metrics(metrics)
        mlflow.log_params(param)
        mlflow.sklearn.log_model(xgbmodel,artifact_path='model')
        mlflow.set_tag('author','Shubham Gupta')
        #mlflow.log_input(x_train)
        
if __name__ == "__main__":
    traindf = ROOT_DIR / 'data' /'processed' / 'train.csv'
    testdf = ROOT_DIR /  'data' /'processed' / 'test.csv'
    model_training(train_path=traindf, test_path=testdf,param=model_param)
    