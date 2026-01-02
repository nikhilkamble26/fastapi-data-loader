from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="Data Loader Microservice",
    version="1.1.0"
)

app.include_router(router)
