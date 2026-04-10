class TransformerConfig:
    """Configuration for the RestaurantTransformer service, including API schema mapping."""
    EXCLUDED_TAGS = {"Deals", "Freebies", "Offers", "Collect stamps"}
    
    # API Schema Keys
    NAME = "name"
    CUISINES = "cuisines"
    RATING = "rating"
    STAR_RATING = "starRating"
    ADDRESS = "address"
    CITY = "city"
    FIRST_LINE = "firstLine"
    POSTAL_CODE = "postalCode"
    LOCATION = "location"
    COORDINATES = "coordinates"
