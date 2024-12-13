import os
import requests
import json
import logging
import time
from dotenv import load_dotenv

load_dotenv()

DISCOURSE_URL = os.getenv("DISCOURSE_URL")
API_KEY = os.getenv("API_KEY")
API_USERNAME = os.getenv("API_USERNAME")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("discourse_users.log"), logging.StreamHandler()]
)

HEADERS = {
    "Api-Key": API_KEY,
    "Api-Username": API_USERNAME,
    "Content-Type": "application/json"
}

RETRY_LIMIT = 3
RATE_LIMIT_DELAY = 1

def create_user(name, email, password, username, active=True, approved=True, external_ids=None):
    url = f"{DISCOURSE_URL}/users.json"
    data = {
        "name": name,
        "email": email,
        "password": password,
        "username": username,
        "active": active,
        "approved": approved
    }

    if external_ids:
        data["external_ids"] = external_ids

    for attempt in range(RETRY_LIMIT):
        try:
            response = requests.post(url, headers=HEADERS, json=data)
            response.raise_for_status()
            logging.info(f"Response for user '{username}': {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as err:
            logging.error(f"Attempt {attempt + 1} failed: {err}")
            time.sleep(2)
    return None

def create_multiple_users(users):
    for user in users:
        name = user.get("name")
        email = user.get("email")
        password = user.get("password")
        username = user.get("username")
        active = user.get("active", True)
        approved = user.get("approved", True)
        external_ids = user.get("external_ids", None)

        response = create_user(name, email, password, username, active, approved, external_ids)

        if response:
            if 'user_id' in response:
                logging.info(f"Created user '{username}' with ID {response['user_id']}")
            else:
                logging.error(f"Failed to create user '{username}', response: {response}")
        else:
            logging.error(f"Failed to create user '{username}'")

        time.sleep(RATE_LIMIT_DELAY)

def load_users_from_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            users = json.load(file)
            return users
    except Exception as e:
        logging.error(f"Failed to load users from file: {e}")
        return []

if __name__ == "__main__":
    users_file = "users.json"
    users = load_users_from_json(users_file)

    if users:
        create_multiple_users(users)
    else:
        logging.error("No users to process. Please check the JSON file.")
