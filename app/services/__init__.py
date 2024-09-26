
from .censo_service import CensoService
from repositories import get_censo_repository

def get_censo_service(connection): 
  repository = get_censo_repository(connection)
  return CensoService(repository)