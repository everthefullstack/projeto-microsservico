from fastapi import FastAPI
from app.presentation.routes import create_routes
from app.presentation.composers.database import create_database
from app.infra.middleware.middleware import ErrorMiddlewareManager


def create_app():

    app: FastAPI = FastAPI()
    app.add_middleware(ErrorMiddlewareManager)
    create_routes(app)
    create_database()

    return app

def create_minimal_app():

    app: FastAPI = FastAPI()
    app.add_middleware(ErrorMiddlewareManager)
    create_routes(app)

    return app