from .api import APIConfig
from .services import ServicesConfig
from .core import CoreConfig

class AppConfig(APIConfig, ServicesConfig, CoreConfig):
    """
    Unified configuration for the entire application.
    Aggregates settings from api/, services/, and core/ sub-packages.
    """
    pass
