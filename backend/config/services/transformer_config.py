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
    NAME_SEPARATORS = [' - ', '|']
    PRIMARY_DELIMITER = ','
    FALLBACK_UNKNOWN_NAME = "Unknown Restaurant"
    FALLBACK_ERROR_NAME = "New Restaurant"

    # Cuisine types that should be treated as "Features" (Tags) rather than primary cuisines.
    # Anything NOT in this list will be treated as a primary cultural cuisine by default.
    FEATURE_CUISINE_TAGS = {
        "Alcohol", "BBQ", "Beauty", "Breakfast", "Brunch", "Bubble Tea", "Burgers", 
        "Burritos", "Cakes", "Chicken", "Coffee", "Convenience", "Crepes", "Curry", 
        "Desserts", "Dim Sum", "Dinner", "Electronics", "Fast Food", "Fish & Chips", 
        "Grill", "Groceries", "Halal", "Hot Dogs", "Kebab", "Lunch", "Milkshakes", 
        "Noodles", "Panini's", "Pasta", "Peri Peri", "Pharmacy", "Pies ", "Pizza", 
        "Pub Food", "Sandwiches", "Shops", "Smoothies", "Steak", "Street Food", 
        "Sushi", "Wraps"
    }