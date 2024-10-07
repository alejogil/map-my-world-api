from datetime import datetime
from app.domains.review.reviewDAO import ReviewDAO
from .reviewModel import ReviewRequest, ReviewResponse

class ReviewService:

    def __init__(self):
        self.dao = ReviewDAO()

    def get_reviews(self) -> list[ReviewResponse]:
        return self.dao.get_reviews()

    def review_location(self, location_id: int, category_id: int):
        review_request = ReviewRequest(location_id=location_id, category_id=category_id)
        return self.dao.create_review(review_request)

    def close_connection(self):
        self.dao.close()
