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

    # Data Cleaning & Fallbacks
    NAME_SEPARATORS = [' - ', '|', ', ']
    PRIMARY_DELIMITER = ','
    FALLBACK_UNKNOWN_NAME = "Unknown Restaurant"
    FALLBACK_ERROR_NAME = "New Restaurant"

    # Primary Cultural Cuisines (Ethnicities).
    # Anything in this list will be treated as a "Primary Cuisine" (Large orange text).
    # Anything NOT in this list (and not a marketing tag) will be treated as a "Specialty Tag".
    CULTURAL_CUISINE_TYPES = {
        "Afghan", "African", "Albanian", "Algerian", "American", "Arabic", "Argentinian", 
        "Armenian", "Asian", "Australian", "Austrian", "Azerbaijani", "Bangladeshi", 
        "Belgian", "Brazilian", "British", "Bulgarian", "Burmese", "Cambodian", 
        "Caribbean", "Chinese", "Colombian", "Cuban", "Cypriot", "Czech", "Danish", 
        "Dutch", "Egyptian", "Ethiopian", "European", "French", "German", "Greek", 
        "Hungarian", "Indian", "Indonesian", "Iranian", "Irish", "Israeli", "Italian", 
        "Jamaican", "Japanese", "Jewish", "Korean", "Kurdish", "Lebanese", "Lithuanian", 
        "Malaysian", "Mediterranean", "Mexican", "Middle Eastern", "Moroccan", 
        "Nepalese", "Nigerian", "Norwegian", "Pakistani", "Persian", "Peruvian", 
        "Philippine", "Polish", "Portuguese", "Romanian", "Russian", "Scandinavian", 
        "Scottish", "South American", "Spanish", "Sri Lankan", "Swedish", "Swiss", 
        "Syrian", "Taiwanese", "Thai", "Tibetan", "Turkish", "Ukrainian", "Vietnamese", 
        "Welsh"
    }