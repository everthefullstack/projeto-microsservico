from dataclasses import dataclass
from sqlmodel import SQLModel
from app.infra.interfaces.database_interface import DatabaseInterface
from app.infra.interfaces.engine_interface import EngineInterface
from app.infra.models.sqlmodel.documento_model import DocumentoModel


@dataclass(slots=True, kw_only=True)
class DatabaseManager(DatabaseInterface):
    
    engine: EngineInterface

    def create_database(self) -> None:
        try:
            SQLModel.metadata.create_all(self.engine.get_engine())
        
        except Exception as e:
            raise e
        