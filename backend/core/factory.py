from fastapi import FastAPI
from config import AppConfig
from .middleware import setup_middleware
from api.routes import router as api_router

def create_app() -> FastAPI:
    """
    The App Factory.
    Manufactures a fully configured FastAPI application instance.
    """
    app = FastAPI(
        title=AppConfig.APP_TITLE,
        description=AppConfig.APP_DESCRIPTION
    )

    # 1. Setup Middleware
    setup_middleware(app)

    # 2. Register Routers
    app.include_router(api_router)

    return app
