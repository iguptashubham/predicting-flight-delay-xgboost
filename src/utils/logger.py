import logging
from pathlib import Path
import datetime as dt 

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
LOG_DIR = ROOT_DIR/'logs'
LOG_DIR.mkdir(parents=True, exist_ok=True)

    
class PathFilter(logging.Filter):
    def filter(self, record):
        # Extract the file name from the full pathname
        record.pathname = Path(record.pathname).name
        return True

def custom_logger(file_name):
    
    file_dir = LOG_DIR / file_name
    file_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a logger
    logger = logging.getLogger(file_name)
    logger.setLevel(logging.DEBUG)
    
    # Create a file handler with date in the filename
    log_date = dt.datetime.now().strftime("%Y-%m-%d")
    log_file = file_dir / f'{log_date}.log'
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    
    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    
    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(pathname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add the custom filter to handlers
    file_handler.addFilter(PathFilter())
    console_handler.addFilter(PathFilter())
    
    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger
