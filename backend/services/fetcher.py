import urllib.request
import json

class JETDataFetcher:
    """
    Dedicated class for network interaction.
    Fully Generic: Receives URL, Postcode, and Headers from the factory.
    Uses urllib to avoid rate-limiting issues with the requests library.
    """
    def __init__(self, base_url: str, postcode: str, headers: dict):
        self.url = f"{base_url}/{postcode}"
        self.headers = headers

    def fetch_raw_restaurants(self):
        """Perform the network request and return raw JSON."""
        try:
            req = urllib.request.Request(self.url, headers=self.headers)
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as e:
            print(f"Network error: {e}")
            return None
