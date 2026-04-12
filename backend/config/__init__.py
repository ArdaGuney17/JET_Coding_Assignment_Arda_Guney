from .api import APIConfig
from .services import ServicesConfig
from .setup import SetupConfig

class AppConfig(APIConfig, ServicesConfig, SetupConfig):
    """
    Unified configuration for the entire application.
    Aggregates settings from api/, services/, and setup/ sub-packages.
    """
    pass
