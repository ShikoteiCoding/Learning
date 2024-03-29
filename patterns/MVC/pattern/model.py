import sqlite3
import os
import logging

DATABASE_PATH = "items.db"


class Model:
    def __init__(self):
        self.items = []
        self.init_db()

    def init_db(self):
        # Should not be here. For the example. (Good practice is a Data Layer Access)

        if os.path.exists(DATABASE_PATH):
            logging.info("Database is already existing.")
            self.conn = sqlite3.connect(DATABASE_PATH)
            return

        with sqlite3.connect(DATABASE_PATH) as self.conn:
            cursor = self.conn.cursor()
            cursor.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT);")
            logging.info("Table has been created.")

    def get_items(self) -> list[str] | None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM items;")
        data = cursor.fetchall()

        if not data:
            return

        return data

    def delete_item(self, id: int) -> int:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM items WHERE id = ?;", (id,))
        return cursor.lastrowid

    def add_item(self, name: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO items (name) VALUES (?);", (name,))
        logging.info(f"Item inserted: {name}")
        return cursor.lastrowid
