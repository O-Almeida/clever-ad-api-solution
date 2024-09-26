# app/utils/unzipper.py

import os
import zipfile
import logging

logger = logging.getLogger(__name__)

class UnzipperError(Exception):
  """
  Custom exception class for handling unzipping errors.
  """
  pass

class Unzipper:
  """
  A utility class for unzipping files and handling file extraction operations.
  """

  @staticmethod
  def unzip_file(zip_file_path: str, extracted_file_path: str) -> str:
    """
    Unzips a file to the specified destination path, maintaining the original file extension, 
    and creating the folder if it doesn't exist.

    Args:
      zip_file_path (str): The path to the zip file.
      extracted_file_path (str): The full path where the file should be extracted.

    Returns:
      extracted_file_with_extension (str): The file path of the extracted file.

    Raises:
      UnzipperError: Exception if the zip file doesn't exist or if there's an issue during extraction.
    """

    logger.debug(f"Starting to unzip file: {zip_file_path}")

    # Check if the zip file exists
    if not os.path.exists(zip_file_path):
      logger.error(f"Zip file does not exist: {zip_file_path}")
      raise UnzipperError(f"Zip file does not exist: {zip_file_path}")

    # Extract the destination folder from the full file path
    destination_folder = os.path.dirname(extracted_file_path)

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
      logger.info(f"Destination folder {destination_folder} does not exist. Creating it.")
      os.makedirs(destination_folder)

    try:
      # Open the zip file
      with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        logger.debug(f"Opened zip file: {zip_file_path}")
        
        # Loop through the files in the zip and extract only the first file
        for file in zip_ref.namelist():
          logger.debug(f"Extracting file: {file}")

          # Extract the first file to the destination folder
          original_file_path = zip_ref.extract(file, destination_folder)
          
          # Get the original file extension
          _, extension = os.path.splitext(file)
          
          # Define the full path with the original extension
          extracted_file_with_extension = extracted_file_path + extension
          
          # Rename the extracted file to the specified path while maintaining the original extension
          os.rename(original_file_path, extracted_file_with_extension)
          
          logger.info(f"File extracted and renamed to: {extracted_file_with_extension}")

          # Stop after renaming the first file and return the new file name
          return extracted_file_with_extension

    except zipfile.BadZipFile as e:
      logger.error(f"Invalid or corrupt zip file: {e}")
      raise UnzipperError(f"Invalid or corrupt zip file: {e}")
    except Exception as e:
      logger.error(f"An unexpected error occurred: {e}")
      raise UnzipperError(f"An unexpected error occurred while extracting the file: {e}")
