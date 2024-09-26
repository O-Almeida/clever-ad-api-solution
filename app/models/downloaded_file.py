# app/models/downloaded_file.py

"""
Module defining the DownloadedFile class.  
"""


from dataclasses import dataclass

@dataclass
class DownloadebleFile:
  """
  Represents a file to be downloaded.

  Attributes:
    id (str): The unique identifier of the file.
    name (str): The name of the file.
    url (str):  The URL to download the file.
  """

  id: str
  name: str
  url: str
