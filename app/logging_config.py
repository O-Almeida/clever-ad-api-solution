# app/logging_config.py


import logging
import os
from datetime import datetime

def setup_logging() -> str:
    """
    Configures logging for the application.
    Creates a new log file per execution with the start time in the filename.
    """

    # Create a timestamp for the log filename
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Get process ID to guarantee uniqueness
    pid = os.getpid()

    # Log filename with timestamp
    log_filename = f"app_{timestamp_str}_{pid}.log"

    # Log directory
    log_dir = os.path.join(os.getcwd(), "app/logs")
    os.makedirs(log_dir, exist_ok=True)

    # Full path to the log file
    log_file_path = os.path.join(log_dir, log_filename)

    # Configure the root logger
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s [%(levelname)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            # Console handler
            logging.StreamHandler(),
            # File handler
            logging.FileHandler(log_file_path)
        ]
    )

    return log_file_path
