from fastapi import FastAPI
from .middleware import setup_middleware
from api.routes import router as api_router

def create_app() -> FastAPI:
    """
    The App Factory.
    Manufactures a fully configured FastAPI application instance.
    """
    app = FastAPI(
        title="JET Restaurant Discovery API",
        description="A God-Tier, fully modular discovery service following the highest architectural standards."
    )

    # 1. Setup Middleware
    setup_middleware(app)

    # 2. Register Routers
    app.include_router(api_router)

    return app
