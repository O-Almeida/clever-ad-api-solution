# app/main.py

from logger import setup_logging

# Set up logging
log_file_path = setup_logging()

from config import Config
from database import DatabaseManager
from api import DocumentDownloadClient
from utils import Unzipper, UnzipperError
from services import get_censo_service

import logging
import os
import shutil

logger = logging.getLogger(__name__)

TMP_FOLDER = Config.TMP_FOLDER
DOWNLOAD_FOLDER = Config.DOWNLOAD_FOLDER

def main():

  logger.info("Intializing automation.")

  # Intialize a database manager
  db_manager = DatabaseManager(Config.DB_HOST, Config.DB_USER, Config.DB_PASSWORD, Config.DB_NAME)

  try:
    # Get the database connection
    db_connection = db_manager.get_connection()

    # Creates an service instance of CensoService
    censo_service = get_censo_service(db_connection)
  

    # Performs a clean up on the old directories
    reset_directories()

    # Retieves all the files to be downaloded
    documents_client = DocumentDownloadClient(Config.API_BASE_URL, TMP_FOLDER)
    # Downalod all the files except for .txt files
    documents_client.download_all_files(Config.API_DOWNLOADS_ENDPOINT, Config.API_DOWNLOADS_PRARMS, [".txt"])
    # Retrieves all the downloaded files
    downloaded_files = os.listdir(TMP_FOLDER)

    # Iterates trought every downloaded file
    for file in downloaded_files:
      
      # Create the full file path
      file_path = os.path.join(TMP_FOLDER, file)
      
      # Try to unzip the file
      try: 
        file_path = Unzipper.unzip_file(
          file_path, 
          os.path.join(DOWNLOAD_FOLDER, os.path.basename(file).split(".zip")[0].strip())
        )
      except UnzipperError as e:
        logger.error(f"Failed to unzip file {file}: {e}")
        continue
      except Exception as e:
        logger.error(f"An unexpected error occurred with file {file}: {e}")
        continue
      
      # Process the data from the excel file and add it to the database
      censo_service.process_excel_data(file_path)

    logger.info("Automation finished with success.")

  except Exception as e:
    logger.error(f"An error occurred: {e}")
  
  finally:
    shutil.rmtree(TMP_FOLDER)
    db_manager.close_connection()


def reset_directories():
  """
    Deletes old directories (if they exist) and creates new empty directories.

    Directories handled:
    - TMP_FOLDER: Temporary files folder.
    - DOWNLOAD_FOLDER: Folder for downloaded files.
  """

  dir_to_delete = [TMP_FOLDER, DOWNLOAD_FOLDER]
  for old_dir in dir_to_delete:
    if os.path.exists(old_dir):
      shutil.rmtree(old_dir)
      logger.info(f"Deleted older direcotrie: {old_dir}") 
    
    os.makedirs(old_dir)
    logger.info(f"Created directorie: {old_dir}") 


if __name__ == "__main__":
    main()