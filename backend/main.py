# The Entry Point Lynchpin
# In the God-Tier Architecture, this file is only a starting point for the Factory.

from setup.startup import create_app

# Manufacture the application instance
JET_app = create_app()

# Note: Start the server with: uvicorn main:JET_app --reload