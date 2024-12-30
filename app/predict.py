import sys
from pathlib import Path

# Add the src directory to sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT_DIR / 'src'
sys.path.append(str(SRC_DIR))

from fastapi import APIRouter, HTTPException
import pandas as pd
from .utils.structure import FlightData
import pickle
from src.build_model import xgbmodel_build  # Import from src

router = APIRouter(
    prefix="/predict",
    tags=["Predict"]
)

@router.post('/')
def predict_delay(userinput: FlightData) -> dict:
    MODEL_PATH = ROOT_DIR / 'models' / 'model.pkl'
    
    # Load the model with error handling
    try:
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
        print("Model loaded successfully.")
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail=f"Error: The file {MODEL_PATH} does not exist.")
    except pickle.UnpicklingError:
        raise HTTPException(status_code=500, detail="Error: The file is not a valid pickle file or is corrupted.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")

    inputs = userinput.dict()
    
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame([inputs])
    try:
        model_output = model.predict(df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")
    
    result = df.to_dict(orient='records')[0]
    
    return {'user_input': result, 'predict_delay': model_output.tolist()}
