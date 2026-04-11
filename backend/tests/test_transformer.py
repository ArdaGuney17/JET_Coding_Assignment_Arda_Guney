import pytest
from services.transformer import RestaurantTransformer

# Let's create a fixture. A fixture is a setup function that Pytest runs before tests.
# It provides our test with a fresh instance of the Transformer to use.
@pytest.fixture
def transformer():
    # We pass an empty set for excluded_tags, as we aren't testing the cuisine logic yet
    return RestaurantTransformer(excluded_tags=set())

class TestTransformerNameCleaning:
    """Testing how the Transformer handles strings with separators and corrupted data."""

    def test_clean_name_with_separators(self, transformer):
        # Normal inputs with messy separators
        assert transformer._clean_name("McDonalds - Branch") == "McDonalds"
        assert transformer._clean_name("Kebab|Shop") == "Kebab"
        assert transformer._clean_name("Pizza - House | Express") == "Pizza"
    
    def test_clean_name_corrupted(self, transformer):
        # Testing what happens when the name is entirely missing or null
        assert transformer._clean_name("") == "Unknown Restaurant"
        assert transformer._clean_name(None) == "Unknown Restaurant"
        
        # Testing what happens if the data type is completely wrong (like a boolean)
        assert transformer._clean_name(False) == "Unknown Restaurant"

class TestTransformerAddressFormatting:
    """Testing how the Transformer builds the address string from pieces."""

    def test_format_address_full(self, transformer):
        # Testing a perfect address from the API
        mock_raw_address = {
            "city": "London",
            "firstLine": "123 Fake Street",
            "postalCode": "W1 1AB"
        }
        assert transformer._format_address(mock_raw_address) == "London, 123 Fake Street, W1 1AB"
        
    def test_format_address_partial_and_missing(self, transformer):
        # Testing when only part of the address is present
        mock_partial = {
            "city": "Manchester",
            "postalCode": "M1"
        }
        # Notice how missing pieces just leave commas. Our frontend knows how to handle raw strings.
        assert transformer._format_address(mock_partial) == "Manchester, , M1"
        
        # Testing a completely empty dict (the fallback when app configuration fails)
        assert transformer._format_address({}) == ""
