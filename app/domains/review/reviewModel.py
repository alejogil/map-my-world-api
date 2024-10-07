from pydantic import BaseModel
from datetime import datetime

class Review(BaseModel):
    id: int
    location_id: int
    category_id: int
    reviewed_at: datetime

class ReviewRequest(BaseModel):
    location_id: int
    category_id: int

class ReviewResponse(ReviewRequest):
    id: int
    reviewed_at: datetime