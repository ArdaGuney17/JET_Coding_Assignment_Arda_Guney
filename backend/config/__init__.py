from .api_config import APIConfig
from .logic_config import LogicConfig

# Export a unified Config object for convenience
class AppConfig(APIConfig, LogicConfig):
    """Unified configuration for the entire application."""
    pass
