from sqlalchemy.sql import text
from sqlalchemy import create_engine

class DatabaseSettings:
    def __init__(self):
        self.engine = create_engine('sqlite:///settings.db')

        with self.get_connection() as connection:
            statement = text("""CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY,
                api_key TEXT,
                wp_api_url TEXT,
                wp_username TEXT,
                wp_password TEXT,
                sleep_time TEXT,
                max_length TEXT
            )""")
            connection.execute(statement)

            statement_2 = text("""CREATE TABLE IF NOT EXISTS suggestions (
            id INTEGER PRIMARY KEY,
            suggestion TEXT
            )""")
            connection.execute(statement_2)

            statement_3 = text("""CREATE TABLE IF NOT EXISTS keywords (
            id INTEGER PRIMARY KEY,
            keyword TEXT
            )""")
            connection.execute(statement_3)

    def get_api_key(self):
        with self.get_connection() as connection:
            statement = text("SELECT * FROM settings WHERE id = 1")
            result = connection.execute(statement)
            row = result.fetchone()
            if row is not None:
                return row[1]
            else:
                return None

    def insert_one(self, api_key, wp_api_url, wp_username, wp_password, sleep_time, max_length):
        with self.get_connection() as connection:
            statement = text(
                "INSERT INTO settings (api_key, wp_api_url, wp_username, wp_password, sleep_time, max_length) VALUES (:api_key, :wp_api_url, :wp_username, :wp_password, :sleep_time, :max_length)")
            connection.execute(statement, {"api_key": api_key, "wp_api_url": wp_api_url, "wp_username": wp_username,
                                           "wp_password": wp_password, "sleep_time": sleep_time,
                                           "max_length": max_length})
            connection.commit()

    def update_one(self, api_key, wp_api_url, wp_username, wp_password, sleep_time, max_length):
        with self.get_connection() as connection:
            statement = text("""UPDATE settings SET 
                                api_key = :api_key, 
                                wp_api_url = :wp_api_url, 
                                wp_username = :wp_username, 
                                wp_password = :wp_password, 
                                sleep_time = :sleep_time, 
                                max_length = :max_length
                                WHERE id = 1""")
            connection.execute(statement, {"api_key": api_key, "wp_api_url": wp_api_url, "wp_username": wp_username,
                                           "wp_password": wp_password, "sleep_time": sleep_time,
                                           "max_length": max_length})
            connection.commit()

    def insert_suggestion(self, suggestion):
        with self.get_connection() as connection:
            statement = text("INSERT INTO suggestions (suggestion) VALUES (:suggestion)")
            connection.execute(statement, {"suggestion": suggestion})
            connection.commit()

    def delete_one_suggestion(self, suggestion):
        with self.get_connection() as connection:
            statement = text("DELETE FROM suggestions WHERE suggestion = :suggestion")
            connection.execute(statement, {"suggestion": suggestion})
            connection.commit()

    def delete_one_keyword(self, keyword):
        with self.get_connection() as connection:
            statement = text("DELETE FROM keywords WHERE keyword = :keyword")
            connection.execute(statement, {"keyword": keyword})
            connection.commit()

    def insert_keyword(self, keyword):
        with self.get_connection() as connection:
            statement = text("INSERT INTO keywords (keyword) VALUES (:keyword)")
            connection.execute(statement, {"keyword": keyword})
            connection.commit()

    def get_all_data(self, table_name):
        with self.get_connection() as connection:
            statement = text(f"SELECT * FROM {table_name}")
            result = connection.execute(statement)
            return result.fetchall()
    def get_connection(self):
        return self.engine.connect()

