from datetime import datetime
from app.providers.sqlite.SQLiteClient import SQLiteClient
from .reviewModel import ReviewRequest, ReviewResponse

class ReviewDAO:

    def __init__(self):
        self.db_client = SQLiteClient()
        self._create_table()

    def _create_table(self):
        self.db_client.execute('''
            CREATE TABLE IF NOT EXISTS location_category_reviewed (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location_id INTEGER NOT NULL,
                category_id INTEGER NOT NULL,
                reviewed_at DATETIME NOT NULL,
                FOREIGN KEY (location_id) REFERENCES locations(id) ON DELETE CASCADE,
                FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
            )
        ''')

    def create_review(self, review: ReviewRequest) -> ReviewResponse:
        reviewed_at = datetime.now()
        self.db_client.execute('''
            INSERT INTO location_category_reviewed (location_id, category_id, reviewed_at)
            VALUES (?, ?, ?)
        ''', (review.location_id, review.category_id, reviewed_at))

        review_id = self.db_client.cursor.lastrowid
        return ReviewResponse(id=review_id, location_id=review.location_id, category_id=review.category_id, reviewed_at=reviewed_at)

    def get_reviews(self) -> list[ReviewResponse]:
        rows = self.db_client.fetchall('''
            SELECT id, location_id, category_id, reviewed_at FROM location_category_reviewed
        ''')

        return [ReviewResponse(id=row[0], location_id=row[1], category_id=row[2], reviewed_at=row[3]) for row in rows]

    def close(self):
        self.db_client.close()
