from app.providers.sqlite.SQLiteClient import SQLiteClient
from .locationModel import LocationRequest, LocationResponse

class LocationDAO:

    def __init__(self):
        self.db_client = SQLiteClient()
        self._create_table()

    def _create_table(self):
        self.db_client.execute('''
            CREATE TABLE IF NOT EXISTS location (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                latitude REAL,
                longitude REAL,
                category_id INTEGER NOT NULL,
                FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE
            )
        ''')

    def create_location(self, location: LocationRequest) -> LocationResponse:
        self.db_client.execute('''
            INSERT INTO location (name, address, latitude, longitude, category_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (location.name, location.address, location.latitude, location.longitude, location.category_id))

        location_id = self.db_client.cursor.lastrowid
        return LocationResponse(id=location_id, **location.dict())

    def get_location(self, location_id: int) -> LocationResponse:
        row = self.db_client.fetchone('''
            SELECT id, name, address, latitude, longitude, category_id FROM location WHERE id = ?
        ''', (location_id,))

        if row:
            return LocationResponse(id=row[0], name=row[1], address=row[2], latitude=row[3], longitude=row[4], category_id=row[5])
        return None
    
    def get_locations(self) -> list[LocationResponse]:
        rows = self.db_client.fetchall('''
            SELECT id, name, address, latitude, longitude, category_id FROM location
        ''')

        return [LocationResponse(id=row[0], name=row[1], address=row[2], latitude=row[3], longitude=row[4], category_id=row[5]) for row in rows]
    
    def get_locations_by_category(self, category_id: int, limit: int = 10) -> list[LocationResponse]:
        rows = self.db_client.fetchall('''
            SELECT id, name, address, latitude, longitude, category_id
            FROM location
            WHERE category_id = ?
            LIMIT ?
        ''', (category_id, limit))

        return [LocationResponse(id=row[0], name=row[1], address=row[2], latitude=row[3], longitude=row[4], category_id=row[5]) for row in rows]


    def close(self):
        self.db_client.close()