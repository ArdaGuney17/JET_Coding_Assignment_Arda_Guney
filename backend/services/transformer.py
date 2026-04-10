from models import Restaurant

class RestaurantTransformer:
    """
    Dedicated class for data logic.
    Input-driven: Receives its excluded_tags set from the constructor.
    """
    def __init__(self, excluded_tags: set):
        self.excluded_tags = excluded_tags

    def transform_to_model(self, raw_item: dict) -> Restaurant:
        """Converts a single raw restaurant dictionary into a Restaurant model."""
        name = self._clean_name(raw_item.get("name"))
        cuisines, tags = self._extract_cuisines_and_tags(raw_item.get("cuisines", []))
        rating = raw_item.get("rating", {}).get("starRating")
        
        raw_address = raw_item.get("address", {})
        address = self._format_address(raw_address)
        
        coordinates = raw_address.get("location", {}).get("coordinates", [])
        lng, lat = (coordinates[0], coordinates[1]) if len(coordinates) == 2 else (None, None)

        return Restaurant(
            name=name,
            cuisines=cuisines,
            rating=rating,
            address=address,
            tags=tags,
            lat=lat,
            lng=lng
        )

    def _clean_name(self, raw_name: str) -> str:
        try:
            name_str = str(raw_name or "")
            if name_str:
                return name_str.replace(' - ', ',').split(',')[0].strip()
            return "Unknown Restaurant"
        except Exception:
            return "New Restaurant"

    def _extract_cuisines_and_tags(self, raw_cuisines: list) -> tuple:
        actual_cuisines = []
        marketing_tags = []
        for cuisine in raw_cuisines:
            name = cuisine.get("name")
            if name:
                if name in self.excluded_tags:
                    marketing_tags.append(name)
                else:
                    actual_cuisines.append(name)
        return ", ".join(actual_cuisines), marketing_tags

    def _format_address(self, raw_address: dict) -> str:
        city = raw_address.get('city', '')
        first_line = raw_address.get('firstLine', '')
        postal_code = raw_address.get('postalCode', '')
        return f"{city}, {first_line}, {postal_code}".strip(", ")
