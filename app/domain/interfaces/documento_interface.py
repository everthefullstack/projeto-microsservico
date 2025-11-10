from abc import ABC, abstractmethod


class DocumentoEntityInterface(ABC):
    @abstractmethod
    def validar_titulo(self) -> None:
        pass

    @abstractmethod
    def validar_conteudo(self) -> None:
        pass

    @abstractmethod
    def validar_autor(self) -> None:
        pass

    @abstractmethod
    def validar_data(self) -> None:
        pass

    @abstractmethod
    def validar_latitude(self) -> None:
        pass

    @abstractmethod
    def validar_longitude(self) -> None:
        pass

