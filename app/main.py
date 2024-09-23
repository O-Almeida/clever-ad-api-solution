# app/main.py

"""
MAin module that orchestrates the workflow of the application.
"""


from app.config import Config
from app.database_manager import DatabaseManager

def main():
    db_manager = DatabaseManager(Config.DB_HOST, Config.DB_USER, Config.DB_PASSWORD, Config.DB_NAME)

if __name__ == "__main__":
    main()