from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SensorData(BaseModel):
    timestamp: datetime
    temperature: float
    humidity: float
    pm25: float
    pm10: float
    co2: float
    voc: float
    # latitude: Optional[float] = None
    # longitude: Optional[float] = None

class PartialSensorData(BaseModel):
    timestamp: datetime
    temperature: float
    humidity: float
    pm25: float
    pm10: float

    class Config:
        from_attributes = True

class UserSettings(BaseModel):
    notifications: bool
    format: str
    thresholds: dict

class UserSettingsCreate(BaseModel):
    notifications: bool
    format: str
    thresholds: dict


class Alert(BaseModel):
    id: int
    timestamp: str
    type: str
    value: float
    threshold: float
    acknowledged: Optional[bool] = False

class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

