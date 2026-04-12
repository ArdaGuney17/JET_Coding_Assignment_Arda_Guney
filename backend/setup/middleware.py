from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from config import AppConfig

def setup_middleware(app: FastAPI):
    """
    Configures security and middleware for the application.
    Separating this allows for easy changes to security policy (CORS, Auth, etc).
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=AppConfig.ALLOWED_ORIGINS, 
        allow_credentials=True,
        allow_methods=AppConfig.ALLOWED_METHODS,
        allow_headers=AppConfig.ALLOWED_HEADERS,
    )
