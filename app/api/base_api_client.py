# app/api/base_api_client.py

"""
Base module for API clients.
"""


import logging
from typing import Optional
import requests

logger = logging.getLogger(__name__)

class BaseAPIClient:
  """
  A base client for making HTTP requests.
  """

  def __init__(self, base_url:str) -> None:
    """
    Initializes the BaseAPIClient with the given base URL.

    Args:
      base_url (str): The base URL for the API.
    """
    self.base_url = base_url

    
  def get(self, endpoint:str, params:Optional[dict]=None, headers:Optional[dict]=None) -> Optional[requests.Response]:
    """
    Makes a GET request to the specified endpoint.

    Args:
      endpoint (str): The API endpoint.
      params (dict, optional): Query parameters.
      headers (dict, optional): Request headers.

    Returns:
      requests (Response): The response object.
    """

    url = f"{self.base_url}{endpoint}"
    try:

      logger.info(f"Making GET request to '{url}'.")

      logger.debug(f"Headers: {headers}'")
      
      response = requests.get(url, params=params, headers=headers)
      response.raise_for_status()

      return response
    
    except requests.RequestException as e:
      
      logger.error(f"GET rquest failed: {e}")
      
      return None
