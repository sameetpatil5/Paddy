# app/main.py

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.routes import router

# FastAPI setup
app = FastAPI(title="Paddy: PDF Tools API")

# Instrumentator setup
Instrumentator().instrument(app).expose(app)

# Include the router
app.include_router(router)
