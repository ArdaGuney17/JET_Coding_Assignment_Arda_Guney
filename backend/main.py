# Setup requirement: run 'pip install fastapi uvicorn requests' in your terminal
# Or install via the requirements file: 'pip install -r requirements.txt'

# Import the necessary libraries to build the API and fetch data
from fastapi import FastAPI
import requests
# Import the CORSMiddleware to allow React app to talk to Python
from fastapi.middleware.cors import CORSMiddleware


# Declared a class to handle the Just Eat API requests and data extraction process in a more flexible and scalable way
# Via the postcode parameter, this class enables the API to be reusable for different postcodes
class JET_API_Client:
    def __init__(self, postcode: str):
        # Target URL for the Just Eat Discovery API (Postcode: CT12EH)
        self.base_url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
        # Mimic a real browser to prevent 403 Forbidden errors from the API
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
            "X-Project-Name": "Arda-JET-Technical-Assessment"
        }
    
    # Method to fetch the raw data from the Just Eat API
    def get_restaurants(self):
        response = requests.get(self.base_url, headers=self.headers)
        # Proceed only if the server responds with a success status (200 OK)
        if response.status_code == 200:
            return response.json()
        return None
    
    # Method to extract the necessary data from the raw data
    def extract_restaurants_data(self, limit: int):
        raw_data = self.get_restaurants()
        # Proceed only if the server responds with a success status (200 OK)
        if raw_data:
            # Isolate the list of restaurants from the full JSON data and get the first 10 restaurants
            # Via the limit parameter, this method enables the API to be reusable for different data limits
            restaurants_list = raw_data.get("restaurants", [])[:limit]
            # Initialize an empty list for our filtered necessary data
            target_data = []
            # Extract only the necessary details name, cuisines, rating and address for each restaurant
            # By adding empty dictionaries {} and empty lists [] as the fallback values, we prevent the API from returning an error if the data is not found
            
            # List of marketing tags to filter out to focus on actual cuisine data 
            excluded_tags = {"Deals", "Freebies", "Offers", "Collect stamps"}
            
            for restaurant in restaurants_list:
                # Cleaning the name of the restaurants from address details
                try:
                    # Forcing whatever is in the 'name' field to be a string
                    # If it's None, it becomes an empty string
                    raw_name = str(restaurant.get("name") or "")

                    if raw_name:
                        # Treat ' - ' and ',' as separators; take the first part and trim extra spaces
                        name = raw_name.replace(' - ', ',').split(',')[0].strip()
                    else:
                        name = "Unknown Restaurant"

                except Exception as e:
                    # If anything goes wrong with one restaurant, don't crash the server!
                    print(f"Error cleaning name: {e}")
                    name = "New Restaurant" # Fallback name
                
                # Extract and filter out the marketing tags from the cuisines list
                raw_cuisines = restaurant.get("cuisines", [])
                filtered_cuisine_names = [
                    cuisine.get("name") 
                    for cuisine in raw_cuisines 
                    if cuisine.get("name") and cuisine.get("name") not in excluded_tags
                ]
                cuisines = ", ".join(filtered_cuisine_names)
                # Extract the "starRating" value from the "rating" dictionary in the raw data to get numeric rating
                rating = restaurant.get("rating", {}).get("starRating")
                # Extract the address dictionary from the raw data 
                raw_address = restaurant.get("address", {})
                # Extract the human readable address details city, firstline and postcode 
                # excluding the coordinates from the raw data and format them into a single string
                address = f"{raw_address.get('city')}, {raw_address.get('firstLine')}, {raw_address.get('postalCode')}"
                # Append the clean dictionary that has the necessary data to our final list
                target_data.append({
                    "name": name,
                    "cuisines": cuisines,
                    "rating": rating,
                    "address": address
                })
            # Return the filtered list with the necessary data
            return target_data
        # Fallback error response if the Just Eat API fails
        return None

# Initialize the FastAPI application
JET_app = FastAPI()

# Allow React app to talk to Python
JET_app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # React Vite server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the root endpoint to extract and filter restaurant data
@JET_app.get("/")
def extract_restaurants_data():
    # Create an instance of the JET_API_Client class with the postcode CT12EH
    JET_client = JET_API_Client("CT12EH")
    # Return the first 10 restaurants from the filtered list with the necessary data
    return JET_client.extract_restaurants_data(10)