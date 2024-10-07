from fastapi import APIRouter, HTTPException
from app.domains.review.reviewService import ReviewService
from app.domains.review.reviewModel import ReviewResponse

router = APIRouter()
service = ReviewService()

@router.get("/", response_model=list[ReviewResponse])
async def get_reviews():
    try:
        reviews = service.get_reviews()
        return reviews
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving reviews: {str(e)}")
