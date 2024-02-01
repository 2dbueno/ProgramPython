import os
import sqlite3

class Database:
    def __init__(self):
        self.create_db_folder()
        self.db_name = os.path.join("db", "users.db")
        self.create_table()

    def create_db_folder(self):
        db_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "db")
        os.makedirs(db_directory, exist_ok=True)

    def get_full_path(self):
        return self.db_name

    def create_table(self):
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def login(self, username, password):
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
                return cursor.fetchone() is not None
        except sqlite3.Error as e:
            print(f"Error during login: {e}")
            return False

    def register(self, username, password):
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM users WHERE username=?", (username,))
                existing_user = cursor.fetchone()
                if existing_user:
                    return False  # User already exists
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                connection.commit()
                return True  # Registration successful
        except sqlite3.Error as e:
            print(f"Error during registration: {e}")
            return False
