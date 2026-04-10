from .fetcher_config import FetcherConfig
from .orchestrator_config import OrchestratorConfig
from .transformer_config import TransformerConfig

class ServicesConfig(FetcherConfig, OrchestratorConfig, TransformerConfig):
    pass
