# app/services/censo_service.py

import logging
from repositories import CensoRepository
from models import Censo
from utils import ExcelTranslator
from typing import List
from uuid import uuid4
import os
import pandas as pd

# Initialize logger
logger = logging.getLogger(__name__)

# Helpers
def isFloat(v: str):
  try:
    float(v)
    return True
  except ValueError:
    return False


class CensoService:
  """
  Service class responsible for Censo model
  """

  def __init__(self, repository: CensoRepository) -> None:
    """
    Initializes the service with a repository.

    Args:
        repository (CensoRepository): A CensoRepository object.
    """
    self.repository = repository

  def process_excel_data(self, file_path: str) -> None:
    """
    Processes an excel file, transforms data into models, and inserts them into the database.

    Args:
        file_path (str): The file path to the excel file to be read.
    """
    logger.debug(f"Starting to process Excel file: {file_path}")

    # Define the transformation function
    def transform_function(row) -> Censo:
      try:
        location_split = row['location'].split(" - ") if ' - ' in row['location'] else [row['location'], None]
        return Censo(
          id=uuid4().hex,
          location=location_split[0],
          state=os.path.basename(file_path).split(".")[0].replace("_", " "),
          state_code=location_split[1],
          value=float(row['value']) if isFloat(row['value']) else None
        )
      except Exception as e:
        logger.error(f"Error transforming row: {row} - {e}")

    try:


      # Read the file and transform data
      models: List[Censo] = ExcelTranslator.read_and_transform(
        file_path=file_path, 
        transform_function=transform_function, 
        names=['location', 'value'], 
        skiprows=1,
        dropna_columns=['location']
      )
      logger.info(f"Successfully transformed {len(models)} rows from {file_path}")

      # Insert the data into the datatable
      self.repository.bulk_insert(models)
      logger.info(f"Successfully inserted {len(models)} records into the database.")
    
    except Exception as e:
      logger.error(f"Failed to process Excel file {file_path}: {e}")
      raise e
