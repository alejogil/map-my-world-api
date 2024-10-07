import sqlite3
from typing import List, Any

class SQLiteClient:

    def __init__(self):
        db_name = "database.db"
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute(self, query: str, params: tuple = ()) -> None:
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self, query: str, params: tuple = ()) -> List[Any]:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query: str, params: tuple = ()) -> Any:
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self) -> None:
        self.connection.close()
