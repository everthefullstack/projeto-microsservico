from abc import ABC, abstractmethod


class DatabaseInterface(ABC):

    @abstractmethod
    def create_database(self) -> None:
        pass
