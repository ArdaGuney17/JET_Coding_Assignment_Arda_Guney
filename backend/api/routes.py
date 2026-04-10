from fastapi import APIRouter, Depends
from services import RestaurantService
from .dependencies import get_restaurant_service

# Create the router instance
router = APIRouter()

# --- THE ROUTES ---

@router.get("/")
def get_restaurants(service: RestaurantService = Depends(get_restaurant_service)):
    """
    Returns the top 10 rated restaurants for the configured postcode.
    The 'service' is automatically assembled by the Dependency Pipeline.
    """
    return service.get_top_rated_restaurants(10)
