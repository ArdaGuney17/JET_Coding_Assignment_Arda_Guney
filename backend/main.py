# Setup requirement: run 'pip install fastapi uvicorn requests' in your terminal
# Or install via the requirements file: 'pip install -r requirements.txt'

# Import the necessary libraries to build the API and fetch data
from fastapi import FastAPI
# Import the CORSMiddleware to allow React app to talk to Python
from fastapi.middleware.cors import CORSMiddleware

# Import your custom class from the services file
from services import JET_API_Client

# Initialize the FastAPI application
JET_app = FastAPI()

# Allow React app to talk to Python
JET_app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the root endpoint to extract and filter restaurant data
@JET_app.get("/")
def get_restaurant_data():
    # The route is now clean and strictly handles the request/response lifecycle
    JET_client = JET_API_Client("CT12EH")
    # Return the first 10 restaurants from the filtered list with the necessary data
    return JET_client.extract_restaurants_data(10)

# --- TEMPORARY ROUTE TO SEE RAW DATA ---
@JET_app.get("/raw")
def get_raw_data():
    # This fetches the data but skips your cleaning functions
    JET_client = JET_API_Client("CT12EH")
    raw_data = JET_client.get_restaurants()
    
    # Return just the first 10 raw restaurant objects
    if raw_data:
        return raw_data.get("restaurants", [])[:10]
    return {"error": "Could not fetch data"}