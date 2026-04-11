import pytest
from services.transformer import RestaurantTransformer
from config.services.transformer_config import TransformerConfig

@pytest.fixture
def transformer():
    # To test logic, we pass a common marketing tag as an excluded tag
    return RestaurantTransformer(excluded_tags={"Deals", "Freebies"})

class TestTransformerNameCleaning:
    def test_clean_name_with_separators(self, transformer):
        assert transformer._clean_name("McDonalds - Branch") == "McDonalds"
        assert transformer._clean_name("Kebab|Shop") == "Kebab"
        assert transformer._clean_name("Pizza - House | Express") == "Pizza"
    
    def test_clean_name_corrupted(self, transformer):
        assert transformer._clean_name("") == "Unknown Restaurant"
        assert transformer._clean_name(None) == "Unknown Restaurant"
        assert transformer._clean_name(False) == "Unknown Restaurant"

class TestTransformerAddressFormatting:
    def test_format_address_full(self, transformer):
        mock_raw_address = {
            "city": "London",
            "firstLine": "123 Fake Street",
            "postalCode": "W1 1AB"
        }
        assert transformer._format_address(mock_raw_address) == "London, 123 Fake Street, W1 1AB"
        
    def test_format_address_partial_and_missing(self, transformer):
        mock_partial = {
            "city": "Manchester",
            "postalCode": "M1"
        }
        assert transformer._format_address(mock_partial) == "Manchester, , M1"
        assert transformer._format_address({}) == ""

class TestTransformerLogic:
    """Testing the inverted ethnicity logic and the overall resilience to fully corrupted data."""

    def test_extract_cuisines_and_tags(self, transformer):
        raw_cuisines = [
            {"name": "Italian"},   # Should become a primary cuisine (ethnicity)
            {"name": "Pizza"},     # Should become a specialty tag (not an ethnicity)
            {"name": "Deals"},     # Should become a marketing tag (excluded)
            {"name": ""}           # Should be safely ignored
        ]
        
        cuisines, marketing, specialty = transformer._extract_cuisines_and_tags(raw_cuisines)
        
        assert cuisines == "Italian"
        assert "Deals" in marketing
        assert "Pizza" in specialty
        
    def test_corrupted_overall_data(self, transformer):
        # We simulate our API throwing a complete fit and returning an empty object.
        # This tests if ALL your default fallbacks work together.
        corrupted_data = {}
        
        restaurant_model = transformer.transform_to_model(corrupted_data)
        
        assert restaurant_model.name == "Unknown Restaurant"
        assert restaurant_model.cuisines == ""
        assert restaurant_model.rating is None
        assert restaurant_model.address == ""
        assert restaurant_model.lat is None
        assert restaurant_model.lng is None
