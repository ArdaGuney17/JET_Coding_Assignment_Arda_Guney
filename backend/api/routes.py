from fastapi import APIRouter, Depends
from services import RestaurantService
from config import AppConfig
from .dependencies import get_restaurant_service

# Create the router instance
router = APIRouter()

# --- THE ROUTES ---

@router.get(AppConfig.RESTAURANT_PATH)
def get_restaurants(service: RestaurantService = Depends(get_restaurant_service)):
    """
    Returns the top-rated restaurants for the configured postcode.
    All parameters (path, limit) are injected from the AppConfig for maximum flexibility.
    """
    return service.get_top_rated_restaurants(AppConfig.DEFAULT_LIMIT)
