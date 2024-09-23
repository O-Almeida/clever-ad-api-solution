# app/api/base_api_client.py

"""
Base module for API clients.
"""


from typing import Optional
import requests


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
    url:str = f"{self.base_url}{endpoint}"
    try:
      response:requests.Response = requests.get(url, params=params, headers=headers)
      response.raise_for_status()
      return response
    except requests.RequestException as e:
      print(f"GET request failed: {e}")
      return None
