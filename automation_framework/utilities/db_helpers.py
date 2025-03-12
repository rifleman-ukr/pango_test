import os
import sqlite3
from automation_framework.utilities.config import config

class DatabaseHelper:
    def __init__(self, db_name=config.get("DB", "DB_NAME")):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def terminate_db(self):
        self.conn.close()
        os.remove(config.get("DB", "DB_NAME"))

    def create_tables(self):
        # Create tables if they don't exist
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                city TEXT PRIMARY KEY,
                temperature REAL,
                feels_like REAL
            )''')

    def insert_weather_data(self, **kwargs):
        args_names = tuple(kwargs.keys())
        args_values = tuple(kwargs.values())
        if "average" in kwargs:
            self.cursor.execute(f"PRAGMA table_info(weather_data)")
            columns = self.cursor.fetchall()
            if not any(column[1] == "average" for column in columns):
                self.cursor.execute(f'''ALTER TABLE weather_data ADD COLUMN average REAL ''')
        self.cursor.execute(f'''INSERT OR REPLACE INTO weather_data {args_names} 
        VALUES {args_values}''')
        self.conn.commit()

    def get_weather_data(self, city):
        self.cursor.execute('''SELECT * FROM weather_data 
        WHERE city=?''', [city.capitalize()])
        _result = self.cursor.fetchall()
        result = {"city": _result[0][0],
                  "temperature": _result[0][1],
                  "feels_like": _result[0][2]}
        if len(_result[0]) == 4:
            result.update({"average": _result[0][3]})
        return result

    def get_hot_city(self):
        self.cursor.execute('''SELECT city, temperature 
        FROM weather_data 
        WHERE average=(SELECT MAX(average) FROM weather_data)''')
        return self.cursor.fetchall()[0]
