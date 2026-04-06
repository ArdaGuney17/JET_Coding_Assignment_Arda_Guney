# Install necessary libraries for backend
# run the following command in the terminal: pip install fastapi uvicorn requests
from fastapi import FastAPI
import requests

# Initialize the FastAPI application for JET Backend
JET_app = FastAPI()

# Define the skeleton for the API
@JET_app.get("/")
def extract_restaurants_data():
    return {"message": "JET Backend Operational"}