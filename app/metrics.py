import json
from fastapi import APIRouter
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
METRICS_PATH = ROOT_DIR / 'reports' / 'metrics.json'
metrics_router = APIRouter(tags=['metrics'], prefix='/metrics')


@metrics_router.get('/')
def get_metrics():
    with open(METRICS_PATH, 'r') as file:
        metric = json.load(file)
    return metric
