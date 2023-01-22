import sqlite3
from decimal import Decimal

from config import DB_PATH


class Database:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path

        sqlite3.register_adapter(Decimal, lambda x: str(x))
        sqlite3.register_converter("PYDECIMAL", lambda x: Decimal(x))

    @staticmethod
    def dict_factory(cursor, row):
        return {
            column[0]: row[index] for index, column in enumerate(cursor.description)
        }

    def insert(self, sensor: str, value: Decimal):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO data (sensor, value) VALUES (?, ?)",
                (sensor, value),
            )
            connection.commit()

    def select(self, limit: int = 5) -> list[dict]:
        with sqlite3.connect(self.db_path) as session:
            session.row_factory = self.dict_factory
            cursor = session.cursor()
            cursor.execute(
                "SELECT sensor, value, datetime "
                "FROM data ORDER BY datetime DESC "
                "LIMIT ?",
                (limit,),
            )
            session.commit()
            return cursor.fetchall()
