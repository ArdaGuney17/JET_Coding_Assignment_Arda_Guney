class AppConfig:
    """
    Centralized Configuration Object.
    Contains all 'Magic Values' for the application to ensure total modularity.
    """
    DEFAULT_POSTCODE = "CT12EH"
    
    API_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
        "X-Project-Name": "Arda-JET-Technical-Assessment"
    }
    
    EXCLUDED_TAGS = {"Deals", "Freebies", "Offers", "Collect stamps"}
