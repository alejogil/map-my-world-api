from datetime import datetime, timedelta
from app.domains.location.locationDAO import LocationDAO
from app.domains.category.categoryDAO import CategoryDAO
from app.domains.review.reviewDAO import ReviewDAO
from .recommenderModel import RecommendationResponse

class RecommenderService:

    def __init__(self):
        self.location_dao = LocationDAO()
        self.category_dao = CategoryDAO()
        self.review_dao = ReviewDAO()

    def get_unreviewed_combinations(self, limit: int = 10) -> list[RecommendationResponse]:
        """
        Main function to get unreviewed location-category combinations.
        Prioritizes combinations that have never been reviewed, followed by
        those not reviewed in the last 30 days.
        """
        
        def _get_never_reviewed_locations() -> list[tuple[int, int]]:
            """
            Retrieves locations that have never been reviewed.
            Each location comes with its associated category.
            :return: List of tuples (location_id, category_id)
            """
            reviewed_combinations_all = _get_all_reviewed_combinations()
            locations = self.location_dao.get_locations()
            
            return [(loc.id, loc.category_id) for loc in locations if (loc.id, loc.category_id) not in reviewed_combinations_all]

        def _get_unreviewed_combinations_last_30_days() -> list[tuple[int, int]]:
            """
            Retrieves locations that have not been reviewed in the last 30 days.
            Each location comes with its associated category.
            :return: List of tuples (location_id, category_id)
            """
            reviewed_combinations_recent = _get_recently_reviewed_combinations()
            locations = self.location_dao.get_locations()

            return [(loc.id, loc.category_id) for loc in locations if (loc.id, loc.category_id) not in reviewed_combinations_recent]

        def _get_recently_reviewed_combinations() -> list[tuple[int, int]]:
            """
            Retrieves combinations that have been reviewed in the last 30 days.
            :return: List of tuples (location_id, category_id) of recently reviewed combinations.
            """
            thirty_days_ago = datetime.now() - timedelta(days=30)
            return [
                (review.location_id, review.category_id)
                for review in self.review_dao.get_reviews()
                if review.reviewed_at > thirty_days_ago
            ]

        def _get_all_reviewed_combinations() -> list[tuple[int, int]]:
            """
            Retrieves all reviewed combinations, regardless of the review date.
            :return: List of tuples (location_id, category_id) of all reviewed combinations.
            """
            return [
                (review.location_id, review.category_id)
                for review in self.review_dao.get_reviews()
            ]

        def _convert_to_response(combinations: list[tuple[int, int]]) -> list[RecommendationResponse]:
            """
            Converts the list of combinations to RecommendationResponse objects.
            Retrieves location and category details (id and name).
            :param combinations: List of tuples (location_id, category_id)
            :return: List of RecommendationResponse objects.
            """
            responses = []
            for loc_id, cat_id in combinations:
                location = self.location_dao.get_location(loc_id)
                category = self.category_dao.get_category(cat_id)

                responses.append(RecommendationResponse(
                    location_id=location.id,
                    location_name=location.name,
                    category_id=category.id,
                    category_name=category.name
                ))
            return responses

        never_reviewed_combinations = _get_never_reviewed_locations()

        if len(never_reviewed_combinations) >= limit:
            return _convert_to_response(never_reviewed_combinations[:limit])

        unreviewed_combinations = _get_unreviewed_combinations_last_30_days()
        combined_combinations = never_reviewed_combinations + unreviewed_combinations[:(limit - len(never_reviewed_combinations))]
        
        return _convert_to_response(combined_combinations[:limit])

    def close_connection(self):
        self.location_dao.close()
        self.category_dao.close()
        self.review_dao.close()
