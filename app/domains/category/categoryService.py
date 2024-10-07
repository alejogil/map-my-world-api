from .categoryDAO import CategoryDAO
from .categoryModel import CategoryRequest, CategoryResponse
from app.domains.review.reviewDAO import ReviewDAO
from app.domains.review.reviewModel import ReviewRequest
from app.domains.location.locationModel import LocationResponse
from app.domains.location.locationDAO import LocationDAO

class CategoryService:

    def __init__(self):
        self.dao = CategoryDAO()
        self.location_dao = LocationDAO()
        self.review_dao = ReviewDAO()

    def create_category(self, category: CategoryRequest) -> CategoryResponse:
        return self.dao.create_category(category)

    def get_categories(self) -> list[CategoryResponse]:
        return self.dao.get_categories()

    def get_category(self, category_id: int) -> CategoryResponse:
        category = self.dao.get_category(category_id)
        if not category:
            raise ValueError(f"Category with id {category_id} not found")
        return category
    
    def get_locations_by_category(self, category_id: int, limit: int = 10) -> list[LocationResponse]:
        locations = self.location_dao.get_locations_by_category(category_id, limit)

        for location in locations:
            review_request = ReviewRequest(location_id=location.id, category_id=category_id)
            self.review_dao.create_review(review_request)

        return locations

    def close_connection(self):
        self.dao.close()
