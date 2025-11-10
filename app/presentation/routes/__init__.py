from fastapi import FastAPI
from app.presentation.routes.documento_routes import documento_routes


def create_routes(app: FastAPI):
    app.include_router(documento_routes)