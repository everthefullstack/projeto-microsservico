from dataclasses import dataclass, field
from sqlmodel import create_engine
from sqlalchemy import event
from sqlalchemy.engine import Engine
from app.infra.interfaces.settings_interface import SettingsInterface
from app.infra.interfaces.engine_interface import EngineInterface
from app.infra.utils.singleton import singleton


@singleton
@dataclass(slots=True, kw_only=True)
class EngineManager(EngineInterface):
    
    __engine: Engine = field(repr=False, init=False)
    __url: str = field(repr=False, init=False)
    settings: SettingsInterface

    def __create_engine(self) -> None:
        self.__url: str = self.settings.get_settings().DATABASE_URL
        self.__engine = create_engine(url=self.__url, echo=False)
        
    def __post_init__(self) -> None:
        self.__create_engine()

    def get_engine(self) -> None:
        return self.__engine
