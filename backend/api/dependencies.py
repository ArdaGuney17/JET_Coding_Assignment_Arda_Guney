from functools import lru_cache
from services import RestaurantService, JETDataFetcher, RestaurantTransformer
from config import AppConfig

# --- THE DEPENDENCY PIPELINE ---

@lru_cache
def _get_data_fetcher() -> JETDataFetcher:
    """Singleton: one JETDataFetcher instance for the lifetime of the process."""
    return JETDataFetcher(
        AppConfig.DISCOVERY_API_URL, 
        AppConfig.DEFAULT_POSTCODE, 
        AppConfig.HEADERS
    )

@lru_cache
def _get_restaurant_transformer() -> RestaurantTransformer:
    """Singleton: one RestaurantTransformer instance for the lifetime of the process."""
    return RestaurantTransformer(AppConfig.EXCLUDED_TAGS)

@lru_cache
def _build_restaurant_service() -> RestaurantService:
    """
    Singleton builder: constructs the RestaurantService exactly once.
    Using lru_cache ensures the same instance (and its in-memory cache) is
    reused on every request, so cached restaurant data actually persists.
    """
    return RestaurantService(
        fetcher=_get_data_fetcher(),
        transformer=_get_restaurant_transformer()
    )

def get_restaurant_service() -> RestaurantService:
    """FastAPI dependency: returns the cached singleton RestaurantService."""
    return _build_restaurant_service()
