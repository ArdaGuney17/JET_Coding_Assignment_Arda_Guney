from pydantic import BaseModel
from typing import List, Optional

class Restaurant(BaseModel):
    """
    Data model representing a cleaned Restaurant entity.
    Using Pydantic ensures type safety and easy serialization.
    """
    name: str
    cuisines: str
    rating: Optional[float]
    address: str
    tags: List[str]
    lat: Optional[float]
    lng: Optional[float]

    class Config:
        from_attributes = True
