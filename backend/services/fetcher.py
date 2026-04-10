import requests

class JETDataFetcher:
    """
    Dedicated class for network interaction.
    Input-driven: Receives postcode and headers from the constructor.
    """
    def __init__(self, postcode: str, headers: dict):
        self.base_url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
        self.headers = headers

    def fetch_raw_restaurants(self):
        """Perform the network request and return raw JSON."""
        try:
            response = requests.get(self.base_url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None
