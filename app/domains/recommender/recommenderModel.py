from pydantic import BaseModel

class RecommendationResponse(BaseModel):
    location_id: int
    location_name: str
    category_id: int
    category_name: str