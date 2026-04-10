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



# --- JET API Client Class ---

# Declared a class to handle the Just Eat API requests and data extraction process in a more flexible and scalable way
# Via the postcode parameter, this class enables the API to be reusable for different postcodes
class JET_API_Client:
    def __init__(self, postcode: str):
        # Target URL for the Just Eat Discovery API (Postcode: CT12EH)
        self.base_url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
        # Mimic a real browser to prevent 403 Forbidden errors from the API
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
            "X-Project-Name": "Arda-JET-Technical-Assessment"
        }
        # Re-added the excluded tags so the tags method has access to it!
        self.excluded_tags = {"Deals", "Freebies", "Offers", "Collect stamps"}
    
    # Method to fetch raw data from the Just Eat API
    def get_restaurants(self):
        response = requests.get(self.base_url, headers=self.headers)
        # Proceed only if the server responds with a success status (200 OK)
        if response.status_code == 200:
            return response.json()
        return None

    # --- HELPER METHODS ---

    # Cleaning the name of the restaurants from address details
    # Forcing whatever is in the 'name' field to be a string
    # If it's None, it becomes an empty string
    # Treat ' - ' and ',' as separators; take the first part and trim extra spaces
    # If anything goes wrong with one restaurant, prevent server from crashing
    def _clean_name(self, raw_name: str) -> str:
        try:
            name_str = str(raw_name or "")
            if name_str:
                return name_str.replace(' - ', ',').split(',')[0].strip()
            return "Unknown Restaurant"
        except Exception as e:
            print(f"Error cleaning name: {e}")
            return "New Restaurant"

    def _extract_cuisines_and_tags(self, raw_cuisines: list) -> tuple:
        """Helper method to separate actual cuisines from marketing tags."""
        actual_cuisines = []
        marketing_tags = []
        
        for cuisine in raw_cuisines:
            name = cuisine.get("name")
            if name:
                # If it's a marketing tag, put it in the tags list
                if name in self.excluded_tags:
                    marketing_tags.append(name)
                # Otherwise, it's a real food cuisine
                else:
                    actual_cuisines.append(name)
                    
        # Return cuisines as a string, and tags as a list
        return ", ".join(actual_cuisines), marketing_tags

    # Extract the human readable address details city, firstline and postcode 
    # excluding the coordinates from the raw data and format them into a single string
    def _format_address(self, raw_address: dict) -> str:
        city = raw_address.get('city', '')
        first_line = raw_address.get('firstLine', '')
        postal_code = raw_address.get('postalCode', '')
        return f"{city}, {first_line}, {postal_code}".strip(", ")

    # --- MAIN ORCHESTRATOR ---

    # Fetches raw data and uses helper methods to build the clean final list
    def extract_restaurants_data(self, limit: int):
        raw_data = self.get_restaurants()
        
        if not raw_data:
            return None

        restaurants_list = raw_data.get("restaurants", [])[:limit]
        target_data = []
        
        for restaurant in restaurants_list:
            name = self._clean_name(restaurant.get("name"))
            cuisines, tags = self._extract_cuisines_and_tags(restaurant.get("cuisines", []))
            # Extract the "starRating" value from the "rating" dictionary in the raw data to get numeric rating
            rating = restaurant.get("rating", {}).get("starRating")
            # Extract the address details from the raw data
            raw_address = restaurant.get("address", {})
            # Format the address details other than coordinates into a single string
            address = self._format_address(raw_address)
            # Extract the coordinates from the raw data
            coordinates = raw_address.get("location", {}).get("coordinates", [])
            
            # Safety check, only extract if both lng and lat exist
            if len(coordinates) == 2:
                lng = coordinates[0] # 1.091004
                lat = coordinates[1] # 51.286542
            else:
                lat = None
                lng = None

            target_data.append({
                "name": name,
                "cuisines": cuisines,
                "rating": rating,
                "address": address,
                "tags": tags,
                "lat": lat,
                "lng": lng
            })

        # Sort the data by rating, highest to lowest. 
        # We use 'or 0' just in case a restaurant is missing a rating to prevent a crash.
        target_data.sort(key=lambda x: x.get('rating') or 0, reverse=True)
            
        return target_data