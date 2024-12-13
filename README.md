Discourse User Management Tool

This tool allows you to manage user accounts on a Discourse platform via its API. It supports creating individual or multiple users using JSON data, with logging and retry mechanisms for error handling.

Features

Create single or multiple users on Discourse using the API.

Load user details from a JSON file.

Retry mechanism for failed API calls.

Logs API responses and errors to a file (discourse_users.log) and console.

Prerequisites

1. Software Requirements

Python 3.7 or higher

Discourse instance with API access enabled

2. Install Required Python Libraries

Install the necessary dependencies using:

pip install -r requirements.txt

Create a requirements.txt file with the following content:

requests
python-dotenv

3. Environment Variables

Create a .env file in the root directory with the following variables:

DISCOURSE_URL=<your_discourse_url>
API_KEY=<your_api_key>
API_USERNAME=<your_api_username>

Replace <your_discourse_url>, <your_api_key>, and <your_api_username> with the appropriate values from your Discourse instance.

Usage

1. Create Users From JSON File

Prepare a JSON file (e.g., users.json) with user details. The structure should be:

[
  {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "password": "securepassword",
    "username": "johndoe",
    "active": true,
    "approved": true
  },
  {
    "name": "Jane Smith",
    "email": "janesmith@example.com",
    "password": "securepassword",
    "username": "janesmith",
    "active": true,
    "approved": true
  }
]

2. Run the Script

Run the script using:

python script.py

The script will:

Load users from the specified JSON file.

Create each user on Discourse.

Log the process and results.

3. Logs

Logs are stored in discourse_users.log and include timestamps, log levels, and messages for debugging and monitoring.

Functions

create_user()

Creates a single user on Discourse.

Arguments:

name: Name of the user

email: Email address

password: Password

username: Username

active: Whether the user is active (default: True)

approved: Whether the user is approved (default: True)

external_ids: Optional external IDs for the user

Returns: Response JSON from the API or None if failed.

create_multiple_users()

Creates multiple users by iterating through a list of user dictionaries.

load_users_from_json()

Loads user data from a JSON file.

Arguments: File path of the JSON file

Returns: A list of user dictionaries

Error Handling

Retries API requests up to 3 times for transient errors.

Logs errors with detailed information for debugging.

License

This project is free to use and distribute.

Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes.
