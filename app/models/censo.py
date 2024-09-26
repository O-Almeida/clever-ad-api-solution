# app/models/censo.py

"""
Module defining the Censo class.  
"""


from dataclasses import dataclass
from typing import Optional

@dataclass
class Censo:
  """
  Represents a Censo.

  Attributes:
    id (str): The unique identifier of the Censo.
    location (str): The name of the location.
    state (str):  The name to the state.
    state_code (str, optional): The code of the state.
    value (float): The value for that location.
  """

  id: str
  location: str
  state: str
  state_code: Optional[str] = None
  value: Optional[float] = None
