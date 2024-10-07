from fastapi import APIRouter, HTTPException
from .recommenderService import RecommenderService

router = APIRouter()

recommender_service = RecommenderService()

@router.get("/")
async def get_recommendations(limit: int = 10):
    try:
        recommendations = recommender_service.get_unreviewed_combinations(limit)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving recommendations: {str(e)}")
