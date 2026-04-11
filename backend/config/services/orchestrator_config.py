class OrchestratorConfig:
    """Configuration for the RestaurantService (Orchestrator)."""
    # Keys used by the orchestrator for top-level data access
    RESTAURANTS = "restaurants"
    # Cache duration in seconds (5 minutes). Prevents hammering the external API.
    CACHE_TTL = 300
