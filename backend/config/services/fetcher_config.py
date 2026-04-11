class FetcherConfig:
    """Configuration for the JETDataFetcher service."""
    DEFAULT_POSTCODE = "BS14DJ"
    DISCOVERY_API_URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Accept": "application/json",
        "Accept-Language": "en-GB,en;q=0.5",
        "Connection": "keep-alive",
        "X-Project-Name": "JET-Coding-Assignment-Arda-Guney"
    }
