# app/utils/excel_reader.py

import pandas as pd
from typing import Callable, List, Any, Dict, Optional

class ExcelTranslator:
  """
  Generic class for reading Excel files and transforming rows into models.
  """
  @staticmethod
  def read_and_transform( file_path: str,
                          transform_function: Callable[[pd.Series], Any],
                          header: Optional[int] = None,
                          names: Optional[List[str]] = None,
                          skiprows: Optional[List[int]] = None,
                          replace_values: Dict[Any, Any] = None,
                          dropna_columns: Optional[List[str]] = None) -> List[Any]:
    """
    Reads an Excel file and transforms each row into a model using the provided transformation function.

    Args:
        file_path (str): The file path to the Excel file.
        transform_function (Callable[[pd.Series], Any]): A function that takes a DataFrame row and returns a model instance.
        header (int or None): Row number to use as the column names. Defaults to None.
        names (List[str]): List of column names to use.
        skiprows (list-like): Rows to skip at the beginning (0-indexed).
        replace_values (Dict[Any, Any]): A dictionary specifying any values that need to be replaced.
        dropna_columns (List[str]): List of columns to check for NaN values and drop the rows.

    Returns:
        List[Any]: A list of model instances
    """
    # Load the Excel file with specified options
    df = pd.read_excel(file_path, header=header, names=names, skiprows=skiprows)

    # If replace_values are provided, replace them
    if replace_values:
      df.replace(replace_values, inplace=True)

    # Drop rows where specified columns have NaN values
    if dropna_columns:
      df.dropna(subset=dropna_columns, inplace=True)

    # Transform each row into a model instance using the provided transform_function
    models = []
    for _, row in df.iterrows():
      model = transform_function(row)
      models.append(model)

    return models
