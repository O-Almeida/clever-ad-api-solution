# app/database_manager.py

"""
Module for managing database connections and operations.
"""

import mysql.connector
from mysql.connector import Error

class DatabaseManager:
  """
  Manages the database connection and operations.
  """

  def __init__(self, host:str, user:str, password:str, database:str) -> None:
    """
    Initializes the DatabaseManager and establishes a database connection.
    
    Args:
      host (str): The database host.
      user (str): The database user.
      password (str): The password for the database user.
      database (str): The name of the database.
    """

    self.connection = None
    try:
      self.connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
      if self.connection.is_connected():
        print("Database connection successful.")
    except Error as e:
      print(f"Error connecting to database: {e}")

  def close_connection(self) -> None:
    """
    Closes the database connection if it is open.
    """
    
    if self.connection is not None and self.connection.is_connected():
      self.connection.close()
      print("Database connection closed.")
