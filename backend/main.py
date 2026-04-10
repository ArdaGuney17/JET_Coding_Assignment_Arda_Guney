# Setup requirement: run 'pip install fastapi uvicorn requests' in your terminal
# Or install via the requirements file: 'pip install -r requirements.txt'

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

# Import our modular packages (Enterprise Package Structure)
from services import RestaurantService, JETDataFetcher, RestaurantTransformer
from config import AppConfig

# --- THE DEPENDENCY PIPELINE ---

def get_data_fetcher() -> JETDataFetcher:
    """Stage 1: The Inlet. Configured via APIConfig."""
    return JETDataFetcher(AppConfig.DEFAULT_POSTCODE, AppConfig.HEADERS)

def get_restaurant_transformer() -> RestaurantTransformer:
    """Stage 2: The Filter. Configured via LogicConfig."""
    return RestaurantTransformer(AppConfig.EXCLUDED_TAGS)

def get_restaurant_service(
    fetcher: JETDataFetcher = Depends(get_data_fetcher),
    transformer: RestaurantTransformer = Depends(get_restaurant_transformer)
) -> RestaurantService:
    """Stage 3: The Assembly Factory. Injects Inlet and Filter into the Pump."""
    return RestaurantService(fetcher, transformer)


# --- APP INITIALIZATION ---
JET_app = FastAPI(title="JET Restaurant Discovery API")

JET_app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- ROUTES ---

@JET_app.get("/")
def get_restaurants(service: RestaurantService = Depends(get_restaurant_service)):
    """The Root endpoint: Strictly returns the pipeline's final product."""
    return service.get_top_rated_restaurants(10)