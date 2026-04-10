# Import the requests library to handle HTTP requests
import requests

from models import Restaurant

# --- OBJECT 1: DATA FETCHER ---

class JETDataFetcher:
    """
    Dedicated class for network interaction.
    Its only responsibility is to talk to the Just Eat API.
    """
    def __init__(self, postcode: str):
        self.base_url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
            "X-Project-Name": "Arda-JET-Technical-Assessment"
        }

    def fetch_raw_restaurants(self):
        """Perform the network request and return raw JSON."""
        try:
            response = requests.get(self.base_url, headers=self.headers)
            response.raise_for_status() # Raise error for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None


# --- OBJECT 2: DATA TRANSFORMER ---

class RestaurantTransformer:
    """
    Dedicated class for data cleaning and object creation.
    It takes raw API dicts and transforms them into clean Restaurant objects.
    """
    def __init__(self):
        self.excluded_tags = {"Deals", "Freebies", "Offers", "Collect stamps"}

    def transform_to_model(self, raw_item: dict) -> Restaurant:
        """Converts a single raw restaurant dictionary into a Restaurant model."""
        name = self._clean_name(raw_item.get("name"))
        cuisines, tags = self._extract_cuisines_and_tags(raw_item.get("cuisines", []))
        rating = raw_item.get("rating", {}).get("starRating")
        
        raw_address = raw_item.get("address", {})
        address = self._format_address(raw_address)
        
        coordinates = raw_address.get("location", {}).get("coordinates", [])
        lng, lat = (coordinates[0], coordinates[1]) if len(coordinates) == 2 else (None, None)

        return Restaurant(
            name=name,
            cuisines=cuisines,
            rating=rating,
            address=address,
            tags=tags,
            lat=lat,
            lng=lng
        )

    def _clean_name(self, raw_name: str) -> str:
        try:
            name_str = str(raw_name or "")
            if name_str:
                return name_str.replace(' - ', ',').split(',')[0].strip()
            return "Unknown Restaurant"
        except Exception:
            return "New Restaurant"

    def _extract_cuisines_and_tags(self, raw_cuisines: list) -> tuple:
        actual_cuisines = []
        marketing_tags = []
        for cuisine in raw_cuisines:
            name = cuisine.get("name")
            if name:
                if name in self.excluded_tags:
                    marketing_tags.append(name)
                else:
                    actual_cuisines.append(name)
        return ", ".join(actual_cuisines), marketing_tags

    def _format_address(self, raw_address: dict) -> str:
        city = raw_address.get('city', '')
        first_line = raw_address.get('firstLine', '')
        postal_code = raw_address.get('postalCode', '')
        return f"{city}, {first_line}, {postal_code}".strip(", ")



# --- OBJECT 3: SERVICE ORCHESTRATOR ---

class RestaurantService:
    """
    The Master Orchestrator.
    It coordinates the Fetcher and the Transformer to provide the final data service.
    """
    def __init__(self, postcode: str):
        self.fetcher = JETDataFetcher(postcode)
        self.transformer = RestaurantTransformer()

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



# 