from pydantic import BaseModel
from typing import List, Optional

class Restaurant(BaseModel):
    """
    The Data Model for a Restaurant.
    Defines the exact structure of our cleaned data.
    """
    name: str
    cuisines: str
    rating: Optional[float]
    address: str
    tags: List[str]
    lat: Optional[float]
    lng: Optional[float]
