# Import the requests library to handle HTTP requests
import requests

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
            address = self._format_address(restaurant.get("address", {}))
            
            # Append the clean dictionary that has the necessary data to our final list
            target_data.append({
                "name": name,
                "cuisines": cuisines,
                "rating": rating,
                "address": address,
                "tags": tags
            })

        # Sort the data by rating, highest to lowest. 
        # We use 'or 0' just in case a restaurant is missing a rating to prevent a crash.
        target_data.sort(key=lambda x: x.get('rating') or 0, reverse=True)
            
        return target_data