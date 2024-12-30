from pathlib import Path
import pickle
import pandas as pd
import pandas as pd
import random
from pydantic import BaseModel, Field
from typing import Optional
import build_model

ROOT_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT_DIR / 'models' / 'model.pkl'
with open(MODEL_PATH,'rb') as file:
    model = pickle.load(file=file)

class FlightData(BaseModel):
    carrier: str
    airport: str
    arr_flights: Optional[float] = Field(None, description="Number of arrival flights")
    arr_del15: Optional[float] = Field(None, description="Number of arrival delays greater than 15 minutes")
    carrier_ct: Optional[float] = Field(None, description="Number of carrier-related delays")
    weather_ct: Optional[float] = Field(None, description="Number of weather-related delays")
    nas_ct: Optional[float] = Field(None, description="Number of National Air System delays")
    security_ct: Optional[float] = Field(None, description="Number of security delays")
    late_aircraft_ct: Optional[float] = Field(None, description="Number of late aircraft delays")
    arr_cancelled: Optional[float] = Field(None, description="Number of canceled arrivals")
    arr_diverted: Optional[float] = Field(None, description="Number of diverted arrivals")
    arr_delay: Optional[float] = Field(None, description="Total arrival delay")
    carrier_delay: Optional[float] = Field(None, description="Total carrier delay")
    weather_delay: Optional[float] = Field(None, description="Total weather delay")
    nas_delay: Optional[float] = Field(None, description="Total National Air System delay")
    security_delay: Optional[float] = Field(None, description="Total security delay")

# Generate random values
flight_data = FlightData(
    carrier="AA",
    airport="JFK",
    arr_flights=random.uniform(50, 200),
    arr_del15=random.uniform(10, 50),
    carrier_ct=random.uniform(5, 30),
    weather_ct=random.uniform(1, 10),
    nas_ct=random.uniform(10, 40),
    security_ct=random.uniform(0, 5),
    late_aircraft_ct=random.uniform(5, 25),
    arr_cancelled=random.uniform(0, 10),
    arr_diverted=random.uniform(0, 5),
    arr_delay=random.uniform(0, 100),
    carrier_delay=random.uniform(0, 50),
    weather_delay=random.uniform(0, 30),
    nas_delay=random.uniform(0, 20),
    security_delay=random.uniform(0, 10)
)

# Convert to DataFrame
flight_data_dict = flight_data.dict()
df = pd.DataFrame([flight_data_dict])
pred = model.predict(df)

print(pred)

    