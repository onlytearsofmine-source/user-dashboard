import logging
import os
from datetime import datetime, timedelta
from typing import List, Dict

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_user_data(user_id: int) -> Dict:
    try:
        # Simulating a database query
        user_data = {
            "id": user_id,
            "name": "John Doe",
            "email": "john@example.com"
        }
        return user_data
    except Exception as e:
        logger.error(f"Failed to retrieve user data: {str(e)}")
        return {}

def get_user_activity(user_id: int) -> List[Dict]:
    try:
        # Simulating a database query
        user_activity = [
            {
                "id": 1,
                "user_id": user_id,
                "activity": "login",
                "timestamp": datetime.now() - timedelta(days=1)
            },
            {
                "id": 2,
                "user_id": user_id,
                "activity": "logout",
                "timestamp": datetime.now() - timedelta(hours=1)
            }
        ]
        return user_activity
    except Exception as e:
        logger.error(f"Failed to retrieve user activity: {str(e)}")
        return []

def write_to_file(file_path: str, data: str) -> bool:
    try:
        with open(file_path, "w") as file:
            file.write(data)
        return True
    except Exception as e:
        logger.error(f"Failed to write to file: {str(e)}")
        return False

def read_from_file(file_path: str) -> str:
    try:
        with open(file_path, "r") as file:
            data = file.read()
        return data
    except Exception as e:
        logger.error(f"Failed to read from file: {str(e)}")
        return ""

def get_config() -> Dict:
    config = {
        "database": {
            "host": os.environ.get("DB_HOST"),
            "port": os.environ.get("DB_PORT"),
            "username": os.environ.get("DB_USERNAME"),
            "password": os.environ.get("DB_PASSWORD")
        }
    }
    return config