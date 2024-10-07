from fastapi import APIRouter, HTTPException
from typing import List
from .locationModel import LocationRequest, LocationResponse
from .locationService import LocationService

router = APIRouter()
service = LocationService()

@router.post("/", response_model=LocationResponse)
async def create_location(location: LocationRequest):
    try:
        return service.create_location(location)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating location: {str(e)}")

@router.get("/{location_id}", response_model=LocationResponse)
async def get_location(location_id: int):
    try:
        location = service.get_location(location_id)
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")
        return location
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving location: {str(e)}")
