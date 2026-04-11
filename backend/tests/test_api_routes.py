import pytest
from fastapi.testclient import TestClient
from main import JET_app
from api.dependencies import get_restaurant_service
from unittest.mock import Mock
from models import Restaurant

# Create a test client using our real FastAPI app
client = TestClient(JET_app)

@pytest.fixture
def mock_service():
    """Create a mock service to bypass the fetcher and transformer completely."""
    return Mock()

class TestAPIRoutes:
    
    def test_get_restaurants_endpoint_success(self, mock_service):
        # 1. Arrange: Setup fake data for the Route
        fake_restaurants = [
            Restaurant(
                name="Test API Restaurant",
                cuisines="Mexican",
                rating=5.0,
                address="123 Route Ave",
                tags=[],
                specialties=[],
                lat=0.0,
                lng=0.0
            )
        ]
        mock_service.get_top_rated_restaurants.return_value = fake_restaurants
        
        # Override the FastAPI dependency injection so it uses our fake service
        # instead of building a real one that hits the internet!
        JET_app.dependency_overrides[get_restaurant_service] = lambda: mock_service
        
        # 2. Act: Pretend to be a web browser and hit our API endpoint
        response = client.get("/")
        
        # Clean up the override so it doesn't affect other tests
        JET_app.dependency_overrides.clear()
        
        # 3. Assert: Verify the API boundaries
        # Did we get a 200 OK?
        assert response.status_code == 200
        
        data = response.json()
        
        # Did it return a list of restaurants?
        assert isinstance(data, list)
        assert len(data) == 1
        
        # Is the data correctly serialized?
        assert data[0]["name"] == "Test API Restaurant"
