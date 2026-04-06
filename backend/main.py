# Install necessary libraries for backend
# run the following command in the terminal: pip install fastapi uvicorn requests
from fastapi import FastAPI
import requests

# Initialize the FastAPI application for JET Backend
JET_app = FastAPI()

# Define the API URL for Just Eat API
API_URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/CT12EH"

# Define the endpoint for the API
@JET_app.get("/")
# Define the function to extract restaurants data
def extract_restaurants_data():
    # Define the headers for the API request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
        "X-Project-Name": "Arda-JET-Technical-Assessment"
    }
    # Send the GET request to the API
    response = requests.get(API_URL, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    
    # Return an error message if the request was not successful
    return {"message": "Failed to extract data", "status_code": response.status_code}