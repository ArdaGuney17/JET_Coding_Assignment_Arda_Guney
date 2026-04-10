# Setup requirement: run 'pip install fastapi uvicorn requests' in your terminal
# Or install via the requirements file: 'pip install -r requirements.txt'

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

# Import our modular OOP components
from services import RestaurantService, JETDataFetcher, RestaurantTransformer

# --- CONFIGURATION ---
# Centralized settings for easy maintenance
DEFAULT_POSTCODE = "CT12EH"

# --- THE DEPENDENCY PIPELINE (PIPELINE FACTORY) ---
# Each function represents a stage in the data processing pipeline.
# This follows the Dependency Inversion Principle (DIP).

def get_data_fetcher() -> JETDataFetcher:
    """Stage 1: The Inlet. Handles raw API communication."""
    return JETDataFetcher(DEFAULT_POSTCODE)

def get_restaurant_transformer() -> RestaurantTransformer:
    """Stage 2: The Filter. Handles data cleaning and business logic."""
    return RestaurantTransformer()

def get_restaurant_service(
    fetcher: JETDataFetcher = Depends(get_data_fetcher),
    transformer: RestaurantTransformer = Depends(get_restaurant_transformer)
) -> RestaurantService:
    """Stage 3: The Pump (The Assembly). Combines the Inlet and Filter into a Service."""
    return RestaurantService(fetcher, transformer)


# --- APP INITIALIZATION ---
JET_app = FastAPI(
    title="JET Restaurant Discovery API",
    description="A professional, pipeline-based discovery service for Just Eat restaurants."
)

JET_app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- THE MAIN ENDPOINT ---

@JET_app.get("/")
def get_restaurants(service: RestaurantService = Depends(get_restaurant_service)):
    """
    Returns the top 10 rated restaurants for the configured postcode.
    The 'service' is automatically assembled by the Pipeline Factory above.
    """
    return service.get_top_rated_restaurants(10)