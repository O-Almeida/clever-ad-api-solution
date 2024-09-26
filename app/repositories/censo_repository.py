# app/repositories/censo_repository.py

from typing import List
from .irepository import IRepository
from models import Censo
from database import DatabaseManager
from mysql.connector import MySQLConnection
import logging

logger = logging.getLogger(__name__)

class CensoRepository(IRepository[Censo]):
  """
  Repository for Censo model.
  """

  def __init__(self, connection:MySQLConnection) -> None:
    """
    Initializes the repository with a database connection.
    
    Args:
        connection (MySQLConnection): A MySQLConnection object.
    """

    self.connection = connection

  def insert(self, model:Censo) -> None:
    """
    Inserts a single Censo into the database.

    Args:
        model (Censo): The Censo model to add.
    """

    query = "INSERT INTO Censos (id, location, state, state_code, value) VALUES (%s, %s, %s, %s, %s)"
    values = (model.id, model.location, model.state, model.state_code, model.value)

    logger.debug(f"Executing query: {query}")
    logger.debug(f"With values: {values}")

    cursor = self.connection.cursor()
    cursor.execute(query, values)
    self.connection.commit()
    cursor.close()

    logger.info(f"Censo with id {model.id} record inserted with success.")

  def bulk_insert(self, models:List[Censo]) -> None:
    """
    Inserts multiple Censo instances into the database.

    Args:
        models (List[Censo]): A liost of Censo models to be added.
    """
    
    query = "INSERT INTO Censos (id, location, state, state_code, value) VALUES (%s, %s, %s, %s, %s)"
    values = [(model.id, model.location, model.state, model.state_code, model.value) for model in models]

    logger.debug(f"Executing query: {query}")
    logger.debug(f"With values: {values}")

    cursor = self.connection.cursor()
    cursor.executemany(query, values)
    self.connection.commit()
    cursor.close()

    logger.info(f"{len(models)} Censo records inserted in the database with success.")