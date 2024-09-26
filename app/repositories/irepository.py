# app/repositories/Irepository.py

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List


# Type variable to be used for any model
T = TypeVar('T')


class IRepository(ABC, Generic[T]):
  """
  Abstarct base class for repositories.
  """

  @abstractmethod
  def insert(self, model:T) -> None:
    """
    Inserts a single model into the database.
    """
    pass

  @abstractmethod
  def bulk_insert(self, models: List[T]) -> None:
    """
    Inserts multiple models into the database.
    """
    pass

