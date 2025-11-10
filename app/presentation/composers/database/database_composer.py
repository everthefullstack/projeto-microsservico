from app.infra.database.database import DatabaseManager
from app.infra.engine.engine import EngineManager
from app.infra.configurations.settings import settings
from typing import Any


class DatabaseComposer:

    @staticmethod
    def compose() -> Any:

        engine = EngineManager(settings=settings)
        database = DatabaseManager(engine=engine)
        return database
