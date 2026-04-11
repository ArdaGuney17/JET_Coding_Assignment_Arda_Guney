from models import Restaurant
from config import AppConfig

class RestaurantTransformer:
    """
    Dedicated class for data logic.
    Input-driven: Receives its excluded_tags set from the constructor.
    """
    def __init__(self, excluded_tags: set):
        self.excluded_tags = excluded_tags

    def transform_to_model(self, raw_item: dict) -> Restaurant:
        """Converts a single raw restaurant dictionary into a Restaurant model."""
        name = self._clean_name(raw_item.get(AppConfig.NAME))
        cuisines, marketing_tags, specialty_tags = self._extract_cuisines_and_tags(raw_item.get(AppConfig.CUISINES, []))
        rating = raw_item.get(AppConfig.RATING, {}).get(AppConfig.STAR_RATING)
        
        raw_address = raw_item.get(AppConfig.ADDRESS, {})
        address = self._format_address(raw_address)
        
        coordinates = raw_address.get(AppConfig.LOCATION, {}).get(AppConfig.COORDINATES, [])
        lng, lat = (coordinates[0], coordinates[1]) if len(coordinates) == 2 else (None, None)

        return Restaurant(
            name=name,
            cuisines=cuisines,
            rating=rating,
            address=address,
            tags=marketing_tags,
            specialties=specialty_tags,
            lat=lat,
            lng=lng
        )

    def _clean_name(self, raw_name: str) -> str:
        try:
            name_str = str(raw_name or "")
            if name_str:
                # Normalize all separators into the primary delimiter
                for sep in AppConfig.NAME_SEPARATORS:
                    name_str = name_str.replace(sep, AppConfig.PRIMARY_DELIMITER)
                return name_str.split(AppConfig.PRIMARY_DELIMITER)[0].strip()
            return AppConfig.FALLBACK_UNKNOWN_NAME
        except Exception:
            return AppConfig.FALLBACK_ERROR_NAME

    def _extract_cuisines_and_tags(self, raw_cuisines: list) -> tuple:
        actual_cuisines = []
        marketing_tags = []
        specialty_tags = []
        for cuisine in raw_cuisines:
            name = cuisine.get(AppConfig.NAME)
            if not name:
                continue

            # Logic: Categorize into Marketing, Specialty, or Primary Cuisine
            if name in self.excluded_tags:
                marketing_tags.append(name)
            elif name in AppConfig.FEATURE_CUISINE_TAGS:
                specialty_tags.append(name)
            else:
                actual_cuisines.append(name)

        return ", ".join(actual_cuisines), marketing_tags, specialty_tags

    def _format_address(self, raw_address: dict) -> str:
        city = raw_address.get(AppConfig.CITY, '')
        first_line = raw_address.get(AppConfig.FIRST_LINE, '')
        postal_code = raw_address.get(AppConfig.POSTAL_CODE, '')
        return f"{city}, {first_line}, {postal_code}".strip(", ")
