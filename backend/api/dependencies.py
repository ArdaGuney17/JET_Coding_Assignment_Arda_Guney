from fastapi import Depends
from services import RestaurantService, JETDataFetcher, RestaurantTransformer
from config import AppConfig

# --- THE DEPENDENCY PIPELINE ---

def get_data_fetcher() -> JETDataFetcher:
    """Stage 1: The Inlet. Configured via APIConfig."""
    return JETDataFetcher(
        AppConfig.DISCOVERY_API_URL, 
        AppConfig.DEFAULT_POSTCODE, 
        AppConfig.HEADERS
    )

def get_restaurant_transformer() -> RestaurantTransformer:
    """Stage 2: The Filter. Configured via LogicConfig."""
    return RestaurantTransformer(AppConfig.EXCLUDED_TAGS)

def get_restaurant_service(
    fetcher: JETDataFetcher = Depends(get_data_fetcher),
    transformer: RestaurantTransformer = Depends(get_restaurant_transformer)
) -> RestaurantService:
    """Stage 3: The Assembly Factory. Injects Inlet and Filter into the Pump."""
    return RestaurantService(fetcher, transformer)
