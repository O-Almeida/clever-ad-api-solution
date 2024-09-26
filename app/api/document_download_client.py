# app/api/document_download_client.py

from models import DownloadebleFile

import logging
import requests
import urllib.request as url_req
from urllib.error import HTTPError
from typing import Optional, List
import uuid
import os

logger = logging.getLogger(__name__)

class DocumentDownloadClient: 
  """
  Client for fetching document downalod URLs from the API and downaloding the files.
  """

  def __init__(self, base_url:str, download_folder:str) -> None:
    """
    Initializes the client with the API base URL and the folder where files will be downaloded.

    Args:
        base_url (str): The base URL for the API
        download_folder (str): The folder where downloaded files will be saved.
    """

    self.base_url = base_url
    self.download_folder = download_folder

  def fetch_documents(self, endpoint:str, params: Optional[dict] = None) -> Optional[List[DownloadebleFile]]:
    """
    Fetches the list of documents from the API.

    Args:
        endpoint (str): The API endpoint to fetch documents.
        params (Optional[dict): Query parameters for the API request-

    Returns:
        Optional[List[DownloadebleFile]]: A list of DownloadbleFile objects, or None if an error occurs.
    """

    url = f"{self.base_url}{endpoint}"
    try:
      logger.debug(f"Making GET request to {url} with params {params}")
      response = requests.get(url, params=params)
      response.raise_for_status()

      data = response.json()
      # Iterate through the response data and create the DownloadbleFile for each file in the response
      files:List[DownloadebleFile] = [
        DownloadebleFile(
          id=uuid.uuid4().hex,
          name=file.get("name"),
          url=file.get("url")
        )
        for file in data
      ]

      logger.info(f"Successfully fetched {len(files)} documents from the API.")
      
      return files
    except requests.RequestException as e:
      logger.error(f"Error fetching documents from API: {e}")

  def download_file(self, downloadble_file:DownloadebleFile) -> Optional[str]:
    """
    Downalod a single file using the pass DownloadbleFile.

    Args:
        downloadble_file (DownloadebleFile): The file to download.

    Returns:
        Optional[str]: The path of the saved file, or None if an error occurs.
    """

    try:
      # Replace " " (spaces) by "%20"
      url = downloadble_file.url.replace(" ", "%20")
      file_path = os.path.join(self.download_folder, downloadble_file.name)

      logger.debug(f"Downloading file from {url} to {file_path}.")
      url_req.urlretrieve(url, file_path)
      logger.info(f"Successfully downloaded {file_path}.")
      return file_path
    except HTTPError as e:
      logger.error(f"Error downloading file {downloadble_file.name}: {e}")
      return None
    
  def download_all_files(self, endpoint:str, params:Optional[dict] = None, extensions_to_ignore:Optional[List[str]] = None) -> None:
    """
    Fetches a list of documents from the API and downalods all of them.

    Args:
        endpoint (str): The API endpoint to fetch documents.
        params (Optional[dict]): Query parameters for the API request.
        file_extension_to_downalod (Optional[List[str]]): A list of file extensions to ignore from downloading. 
    """

    # Fetch documents information from the API
    documents = self.fetch_documents(endpoint, params)
    if not documents:
      logger.warning("No documents to downalod or an error occurred while fetching documents.")
      return
    
    # Downalod each document
    for document in documents:

      # Extract the file extension
      _, file_extension = os.path.splitext(document.name)

      # Validate if file extension is to ignore
      if file_extension in (extensions_to_ignore or []):
        logger.info(f"Ignoring file {document.name} due it extension {file_extension}.")
        continue

      # Download file
      self.download_file(document)

