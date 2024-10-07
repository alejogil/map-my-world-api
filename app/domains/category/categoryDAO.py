from app.providers.sqlite.SQLiteClient import SQLiteClient
from .categoryModel import CategoryRequest, CategoryResponse

class CategoryDAO:

    def __init__(self):
        self.db_client = SQLiteClient()
        self._create_table()

    def _create_table(self):
        self.db_client.execute('''
            CREATE TABLE IF NOT EXISTS category (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL
            )
        ''')

    def create_category(self, category: CategoryRequest) -> CategoryResponse:
        self.db_client.execute('''
            INSERT INTO category (name, description)
            VALUES (?, ?)
        ''', (category.name, category.description))

        category_id = self.db_client.cursor.lastrowid
        return CategoryResponse(id=category_id, **category.dict())

    def get_categories(self) -> list[CategoryResponse]:
        rows = self.db_client.fetchall('''
            SELECT id, name, description FROM category
        ''')

        return [CategoryResponse(id=row[0], name=row[1], description=row[2]) for row in rows]

    def get_category(self, category_id: int) -> CategoryResponse:
        row = self.db_client.fetchone('''
            SELECT id, name, description FROM category WHERE id = ?
        ''', (category_id,))

        if row:
            return CategoryResponse(id=row[0], name=row[1], description=row[2])
        return None

    def close(self):
        self.db_client.close()
