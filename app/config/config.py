# app/config.py

import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

class Config:
  """
  Configuration class that holds database, API configurations and directory configurations.
  """

  # Database configuration
  DB_HOST = os.getenv('DB_HOST', 'db')
  DB_USER = os.getenv('DB_USER', 'root')
  DB_PASSWORD = os.getenv('DB_PASSWORD', '')
  DB_NAME = os.getenv('DB_NAME', 'db')

  # API configuration
  API_BASE_URL = "https://servicodados.ibge.gov.br/api/v1"
  API_DOWNLOADS_ENDPOINT = "/downloads/estatisticas"
  API_DOWNLOADS_PRARMS = {"caminho":"Censos/Censo_Demografico_1991/Indice_de_Gini"}

  # Directory configurations
  DOWNLOAD_FOLDER = f"{str(Path(__file__).parents[1])}/download/"
  TMP_FOLDER = f"{str(Path(__file__).parents[1])}/tmp/"
