import logging
import os
from datetime import datetime


def get_logger(name: str = "automation_logger") -> logging.Logger:
    """
    Creates and returns a configured Python logger instance that logs
    to both console and a daily log file under logs/.
    """
    logger = logging.getLogger(name)

    # Avoid adding multiple handlers if logger is already configured
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # Define Log Format
    log_format = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # 1. Console Handler (Logs output in terminal)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # 2. File Handler (Saves logs to file inside logs/ folder)
    logs_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_dir, exist_ok=True)

    log_file_name = f"automation_{datetime.now().strftime('%Y-%m-%d')}.log"
    log_file_path = os.path.join(logs_dir, log_file_name)

    file_handler = logging.FileHandler(log_file_path, mode="a")
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    return logger