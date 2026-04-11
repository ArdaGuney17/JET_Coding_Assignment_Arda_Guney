import time
from .fetcher import JETDataFetcher
from .transformer import RestaurantTransformer
from config import AppConfig

class RestaurantService:
    """
    The Master Orchestrator (The Pump).
    It coordinates the Fetcher and the Transformer to provide the final data service.
    Implements in-memory caching to prevent excessive external API calls (429 errors).
    """
    def __init__(self, fetcher: JETDataFetcher, transformer: RestaurantTransformer):
        self.fetcher = fetcher
        self.transformer = transformer
        self._cache = None
        self._cache_timestamp = 0

    def get_top_rated_restaurants(self, limit: int = AppConfig.DEFAULT_LIMIT):
        """
        Fetch, transform, sort, and return a list of Restaurant objects.
        Results are cached for CACHE_TTL seconds to reduce external API load.
        """
        now = time.time()
        cache_age = now - self._cache_timestamp

        # Return cached result if it's still fresh
        if self._cache is not None and cache_age < AppConfig.CACHE_TTL:
            print(f"Cache hit! Returning cached data ({int(AppConfig.CACHE_TTL - cache_age)}s remaining).")
            return self._cache

        # Cache is stale or empty — fetch fresh data
        print("Cache miss. Fetching fresh data from Just Eat API...")
        raw_data = self.fetcher.fetch_raw_restaurants()
        if not raw_data or AppConfig.RESTAURANTS not in raw_data:
            return []

        raw_list = raw_data.get(AppConfig.RESTAURANTS, [])[:limit]

        # Transform raw dicts into Restaurant objects
        restaurants = [self.transformer.transform_to_model(item) for item in raw_list]

        # Sort by rating (highest to lowest)
        restaurants.sort(key=lambda x: x.rating or 0, reverse=True)

        # Store in cache with a fresh timestamp
        self._cache = restaurants
        self._cache_timestamp = now

        return restaurants
