# app/database_manager.py

import logging
import mysql.connector
from mysql.connector import Error

logger = logging.getLogger(__name__)

class DatabaseManager:
  """
  Singleton class that manages the database connection and operations.
  """

  _instance = None

  def __new__(cls, *args, **kwargs):
    """
    Ensures only one instance of DatabaseManager is created.
    """
    if cls._instance is None:
      cls._instance = super(DatabaseManager, cls).__new__(cls)
    return cls._instance

  def __init__(self, host:str, user:str, password:str, database:str) -> None:
    """
    Initializes the DatabaseManager and establishes a database connection.

    Args:
      host (str): The database host.
      user (str): The database user.
      password (str): The password for the database user.
      database (str): The name of the database.
    """
    if not hasattr(self, "connection"):
      self.connection = None
      self._connect(host, user, password, database)

  def _connect(self, host:str, user:str, password:str, database:str) -> None:
    """
    Establishes a database connection.
    """
    try:
      self.connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
      if self.connection.is_connected():
        logger.info("Database connection successful.")
    except Error as e:
      logger.error(f"Error connecting to database: {e}")

  def get_connection(self):
    """
    Returns the database connection if it is established, otherwise raises an error.
    """
    if self.connection is None or not self.connection.is_connected():
      raise Error("No database connection established.")
    return self.connection

  def close_connection(self) -> None:
    """
    Closes the database connection if it is open.
    """
    if self.connection is not None and self.connection.is_connected():
      self.connection.close()
      logger.info("Database connection closed.")
