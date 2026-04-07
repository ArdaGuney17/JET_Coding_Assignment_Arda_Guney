# Setup requirement: run 'pip install fastapi uvicorn requests' in your terminal
# Or install via the requirements file: 'pip install -r requirements.txt'

# Import the necessary libraries to build the API and fetch data
from fastapi import FastAPI
import requests

# Initialize the FastAPI application
JET_app = FastAPI()

# Target URL for the Just Eat Discovery API (Postcode: CT12EH)
API_URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/CT12EH"

# Define the root endpoint to extract and filter restaurant data
@JET_app.get("/")
def extract_restaurants_data():
    # Mimic a real browser to prevent 403 Forbidden errors from the API
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
        "X-Project-Name": "Arda-JET-Technical-Assessment"
    }
    
    # Fetch the live data from Just Eat
    response = requests.get(API_URL, headers=headers)
    
    # Proceed only if the server responds with a success status (200 OK)
    if response.status_code == 200:
        raw_data = response.json()

        # Isolate the list of restaurants from the full JSON data and get the first 10 restaurants
        restaurants_list = raw_data.get("restaurants", [])[:10]

        # Initialize an empty list for our filtered necessary data
        target_data = []

        # Extract only the necessary details name, cuisines, rating and address for each restaurant
        # By adding empty dictionaries {} and empty lists [] as the fallback values, we prevent the API from returning an error if the data is not found
        for restaurant in restaurants_list:
            name = restaurant.get("name")
            # Extract the cuisines list from the raw data
            raw_cuisines = restaurant.get("cuisines", [])
            # Extract the "name" value from the each cuisine dictionary in the raw cuisines list and format them into a single string
            cuisines_list = f"{', '.join([cuisine.get("name") for cuisine in raw_cuisines if cuisine.get("name")])}"
            # Extract the "starRating" value from the "rating" dictionary in the raw data
            rating = restaurant.get("rating", {}).get("starRating")
            # Extract the address dictionary from the raw data 
            raw_address = restaurant.get("address", {})
            # Extract the address details from the raw data and format them into a single string
            clean_adress = f"{raw_address.get('city')}, {raw_address.get('firstLine')}, {raw_address.get('postalCode')}, {raw_address.get('location', {}).get('coordinates', [])}"
            
            # Append the clean dictionary that has the necessary data to our final list
            target_data.append({
                "name": name,
                "cuisines": cuisines_list,
                "rating": rating,
                "address": clean_adress
            })  

        # Return the filtered list with the necessary data
        return target_data
    
    # Fallback error response if the Just Eat API fails
    return {"message": "Failed to extract data", "status_code": response.status_code}