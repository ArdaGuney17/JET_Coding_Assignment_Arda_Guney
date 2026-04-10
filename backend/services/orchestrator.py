from .fetcher import JETDataFetcher
from .transformer import RestaurantTransformer

class RestaurantService:
    """
    The Master Orchestrator (The Pump).
    It coordinates the Fetcher and the Transformer to provide the final data service.
    Follows 'Dependency Inversion' by receiving its dependencies via injection.
    """
    def __init__(self, fetcher: JETDataFetcher, transformer: RestaurantTransformer):
        self.fetcher = fetcher
        self.transformer = transformer

    def get_top_rated_restaurants(self, limit: int = 10):
        """Fetch, transform, sort, and return a list of Restaurant objects."""
        raw_data = self.fetcher.fetch_raw_restaurants()
        if not raw_data or "restaurants" not in raw_data:
            return []

        raw_list = raw_data.get("restaurants", [])[:limit]
        
        # Transform raw dicts into Restaurant objects
        restaurants = [self.transformer.transform_to_model(item) for item in raw_list]

        # Sort by rating (highest to lowest)
        restaurants.sort(key=lambda x: x.rating or 0, reverse=True)

        return restaurants
