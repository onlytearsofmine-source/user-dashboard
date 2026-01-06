import logging
import os
from datetime import datetime

def configure_logging(log_level='INFO'):
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s', 
        datefmt='%Y-%m-%d %H:%M:%S', 
        level=getattr(logging, log_level.upper())
    )

def get_project_root() -> str:
    return os.path.dirname(os.path.dirname(__file__))

def get_current_timestamp() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def validate_input(input_data: dict, required_fields: list) -> bool:
    for field in required_fields:
        if field not in input_data:
            logging.error(f"Missing required field: {field}")
            return False
    return True

class Utils:
    def __init__(self):
        self.log_level = 'INFO'

    def set_log_level(self, log_level: str):
        self.log_level = log_level
        configure_logging(log_level)

    def get_user_data(self, user_id: int) -> dict:
        # Implement logic to fetch user data from database or API
        # For now, return dummy data
        return {'user_id': user_id, 'name': 'John Doe', 'email': 'johndoe@example.com'} 

# Initialize the Utils class
utils = Utils()