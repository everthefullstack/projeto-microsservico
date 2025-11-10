from dataclasses import dataclass
from typing import Any, Optional
from sqlmodel import Session
from app.infra.interfaces.engine_interface import EngineInterface
from app.infra.interfaces.session_interface import SessionInterface


@dataclass(slots=True, kw_only=True)
class SessionManager(SessionInterface):
    
    engine: EngineInterface
    __session: Optional[Session] = None

    def __create_session(self) -> None:
        self.__session = Session(self.engine.get_engine())
        
    def __post_init__(self) -> None:
        self.__create_session()

    def get_session(self) -> Any:
        return self.__session
    