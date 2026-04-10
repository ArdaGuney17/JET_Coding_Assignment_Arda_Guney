import requests

class JETDataFetcher:
    """
    Dedicated class for network interaction.
    Fully Generic: Receives URL, Postcode, and Headers from the factory.
    """
    def __init__(self, base_url: str, postcode: str, headers: dict):
        self.url = f"{base_url}/{postcode}"
        self.headers = headers

    def fetch_raw_restaurants(self):
        """Perform the network request and return raw JSON."""
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None
