from dotenv import load_dotenv
import requests
import os


# Load environment variables from .env file
load_dotenv()

# Function to handle user login and generate a token
def login():
    email = os.getenv("ADMIN_EMAIL")
    password = os.getenv("ADMIN_PASSWORD")
    # Make a request to your login API endpoint to authenticate the user and obtain a token
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(f"{os.getenv('API_ENDPOINT')}/api/login/", json=data)
    if response.status_code == 200:
        tokens = response.json()
        return tokens
    else:
        print("Login failed. Please try again.")
        return None
        
# Validate Token
def validate_token(token):
    # Make a request to your login API endpoint to authenticate the user and obtain a token
    data = {
        "token": token
    }
    response = requests.post(f"{os.getenv('API_ENDPOINT')}/api/token/verify/", json=data)
    if response.status_code == 200:
        return True
    else:
        return False

# Refresh Token
def refresh_token(token):
    # Make a request to your login API endpoint to authenticate the user and obtain a token
    data = {
        "refresh": token
    }
    response = requests.post(f"{os.getenv('API_ENDPOINT')}/api/token/refresh/", json=data)
    if response.status_code == 200:
        tokens = response.json()
        return tokens
    else:
        print("Token refresh failed. Please try again.")
        return None


__all__ = [
    "login",
    "validate_token",
    "refresh_token",
]
