# app/main.py

from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="Paddy: PDF Tools API")

app.include_router(router)
