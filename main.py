from fastapi import FastAPI
import uvicorn
from src import build_model
from app.predict import router as predict_router
from app.metrics import metrics_router as metric_router

app = FastAPI(title='Flight Delay Prediction')

app.include_router(predict_router)
app.include_router(metric_router)

@app.get("/")  # Define the root endpoint
async def read_root():
    return {"message": "Welcome to the Flight Delay Prediction API"}

if __name__ == "__main__":
    uvicorn.run(app, port=5000)
