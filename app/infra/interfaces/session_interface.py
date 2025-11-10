from abc import ABC, abstractmethod


class SessionInterface(ABC):
    
    @abstractmethod
    def get_session(self) -> None:
        pass
    