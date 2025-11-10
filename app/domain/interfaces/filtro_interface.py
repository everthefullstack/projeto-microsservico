from abc import ABC, abstractmethod


class FiltroInterface(ABC):
    @abstractmethod
    def validar_buscar(self) -> None:
        pass
