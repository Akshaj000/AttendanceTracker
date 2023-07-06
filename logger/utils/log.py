from dotenv import load_dotenv
import requests
import os
import geocoder


# Load environment variables from .env file
load_dotenv()

# Function to get location based on IP address
def get_location():
    g = geocoder.ip('me')
    if g:
        location = g.city + ", " + g.state + ", " + g.country
        return location
    else:
        print("Failed to retrieve location information.")
        return None

# Function to make a request to the log API with the provided token, MAC address, and IP address
def log_event(device, token):
    mac_address = device["mac"]
    ip_address = device["ip"]
    # Get location information based on IP address
    location_data = get_location()
    # Make a request to your log API endpoint with the token, MAC address, and IP address
    headers = {
        "Authorization": f"Bearer {token}",
    }
    json = {
        "mac_address" : mac_address,
        "meta": {
            "ip_address": ip_address,
            "location": location_data
        }
    }
    response = requests.post(
         f"{os.getenv('API_ENDPOINT')}/api/device/log/", 
        headers=headers,
        json=json
    )
    if response.status_code == 201:
        print(response.json()['message'])
    else:
        print(response.json()['message'])


__all__ = [
    "log_event",
]
