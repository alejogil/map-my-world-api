from pydantic import BaseModel

class Location(BaseModel):
    id: int
    name: str
    address: str
    latitude: float
    longitude: float
    category_id: int

class LocationRequest(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float
    category_id: int

class LocationResponse(LocationRequest):
    id: int