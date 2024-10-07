from fastapi import APIRouter, HTTPException
from typing import List
from .categoryService import CategoryService
from .categoryModel import CategoryRequest, CategoryResponse
from app.domains.location.locationModel import LocationResponse

router = APIRouter()
category_service = CategoryService()

@router.post("/", response_model=CategoryResponse)
async def create_category(category: CategoryRequest):
    try:
        return category_service.create_category(category)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=list[CategoryResponse])
async def get_categories():
    try:
        return category_service.get_categories()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/{category_id}/locations", response_model=list[LocationResponse])
async def get_locations_by_category(category_id: int, limit: int = 10):
    try:
        locations = category_service.get_locations_by_category(category_id, limit)
        return locations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving locations: {str(e)}")