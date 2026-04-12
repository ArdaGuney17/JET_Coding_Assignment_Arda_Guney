import pytest
from unittest.mock import Mock
from fastapi import HTTPException
from services.orchestrator import RestaurantService
from services.fetcher import JETDataFetcher
from services.transformer import RestaurantTransformer
from config.services.transformer_config import TransformerConfig

@pytest.fixture
def mock_fetcher():
    """Create a fake fetcher that doesn't use the internet."""
    return Mock(spec=JETDataFetcher)

@pytest.fixture
def real_transformer():
    """Use the real transformer so I can see the full data flow."""
    return RestaurantTransformer(excluded_tags=set())

@pytest.fixture
def restaurant_service(mock_fetcher, real_transformer):
    """Provide a service instance wired with my fake fetcher."""
    return RestaurantService(fetcher=mock_fetcher, transformer=real_transformer)

class TestRestaurantServiceMocking:
    
    def test_get_top_rated_restaurants_success(self, restaurant_service, mock_fetcher):
        # 1. Arrange: Setup the fake data I want the mock to return
        fake_api_response = {
            "restaurants": [
                {
                    "name": "Mocked Pizza Place",
                    "rating": {"starRating": 4.5},
                    "cuisines": [{"name": "Italian"}]
                },
                {
                    "name": "Mocked Burger Joint",
                    "rating": {"starRating": 4.8},
                    "cuisines": [{"name": "American"}]
                }
            ]
        }
        # Tell the fake fetcher to return my fake data instead of calling the internet
        mock_fetcher.fetch_raw_restaurants.return_value = fake_api_response
        
        # 2. Act: Call the service method
        # This will call my mock_fetcher under the hood!
        results = restaurant_service.get_top_rated_restaurants(limit=2)
        
        # 3. Assert: Verify the results
        assert len(results) == 2
        # Verify the orchestrator correctly sorted them by rating (4.8 > 4.5)
        assert results[0].name == "Mocked Burger Joint"
        assert results[1].name == "Mocked Pizza Place"
        
        # Verify the mock was actually called exactly once
        mock_fetcher.fetch_raw_restaurants.assert_called_once()

    def test_get_top_rated_restaurants_api_failure(self, restaurant_service, mock_fetcher):
        # 1. Arrange: Tell the fetcher to simulate an internet outage or API crash
        mock_fetcher.fetch_raw_restaurants.side_effect = HTTPException(status_code=500, detail="JustEat API Down")
        
        # 2 & 3. Act & Assert: Verify that the service gracefully propagates the error 
        # so the API endpoint can catch it and show an error state to the user.
        with pytest.raises(HTTPException) as exc_info:
            restaurant_service.get_top_rated_restaurants()
            
        assert exc_info.value.status_code == 500
        assert exc_info.value.detail == "JustEat API Down"
