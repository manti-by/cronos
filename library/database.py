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

    def insert(self, t1: Decimal, t2: Decimal, t3: Decimal, t4: Decimal, t5: Decimal):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO data (t1, t2, t3, t4, t5) VALUES (?, ?, ?, ?, ?)",
                (t1, t2, t3, t4, t5),
            )
            connection.commit()

    def latest(self) -> dict:
        with sqlite3.connect(self.db_path) as session:
            session.row_factory = self.dict_factory
            cursor = session.cursor()
            cursor.execute("SELECT * FROM data ORDER BY datetime DESC")
            session.commit()
            return cursor.fetchone()
