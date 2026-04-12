from fastapi import Depends
from services import RestaurantService, JETDataFetcher, RestaurantTransformer
from config import AppConfig

# --- THE DEPENDENCY PIPELINE ---

def get_data_fetcher() -> JETDataFetcher:
    """Provides a configured JETDataFetcher instance."""
    return JETDataFetcher(
        AppConfig.DISCOVERY_API_URL, 
        AppConfig.DEFAULT_POSTCODE, 
        AppConfig.HEADERS
    )

def get_restaurant_transformer() -> RestaurantTransformer:
    """Provides a configured RestaurantTransformer instance."""
    return RestaurantTransformer(AppConfig.EXCLUDED_TAGS)

def get_restaurant_service(
    fetcher: JETDataFetcher = Depends(get_data_fetcher),
    transformer: RestaurantTransformer = Depends(get_restaurant_transformer)
) -> RestaurantService:
    """Combines fetcher and transformer into a unified RestaurantService."""
    return RestaurantService(fetcher, transformer)
