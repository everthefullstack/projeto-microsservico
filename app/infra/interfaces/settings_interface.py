from abc import ABC, abstractmethod
from dynaconf import Dynaconf


class SettingsInterface(ABC):

    @abstractmethod
    def get_settings(self) -> Dynaconf:
        pass
    