from .middleware_config import MiddlewareConfig
from .startup_config import StartupConfig

class SetupConfig(MiddlewareConfig, StartupConfig):
    pass
