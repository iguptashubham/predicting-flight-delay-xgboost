from pydantic import BaseModel, Field
from typing import Optional

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

