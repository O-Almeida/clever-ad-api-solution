

from .censo_repository import CensoRepository
from database import DatabaseManager
from config import Config

def get_censo_repository(connection):
  # Initialize the database connection
  return CensoRepository(connection)