# app/config.py

"""
Configuration module for the application.
Handles environment varibales and configuration settings.
"""


import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
  """
  Configuration class that holds database and API configurations.
  """

  # Database configuration
  DB_HOST = os.getenv('DB_HOST', 'db')
  DB_USER = os.getenv('DB_USER', 'root')
  DB_PASSWORD = os.getenv('DB_PASSWORD', '')
  DB_NAME = os.getenv('DB_NAME', 'db')

  # API configuration
  API_BASE_URL = "https://servicodados.ibge.gov.br/api/v1/downloads/estatisticas?caminho=Censos/Censo_Demografico_1991/Indice_de_Gini"
