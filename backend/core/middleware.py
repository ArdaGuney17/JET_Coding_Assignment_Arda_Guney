from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def setup_middleware(app: FastAPI):
    """
    Configures security and middleware for the application.
    Separating this allows for easy changes to security policy (CORS, Auth, etc).
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"], 
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
