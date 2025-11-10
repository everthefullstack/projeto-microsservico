from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.documento_entity import DocumentoEntity
from app.domain.entities.filtro_entity import FiltroEntity


class CriarDocumentoUseCaseInterface(ABC):
    @abstractmethod
    def criar_documento(self, documento_entity: DocumentoEntity) -> DocumentoEntity:
        pass

class BuscarDocumentoUseCaseInterface(ABC):
    @abstractmethod
    def buscar_documentos(self, filtro_entity: FiltroEntity) -> Optional[List[DocumentoEntity]]:
        pass

class DocumentoRepositoryInterface(ABC):
    @abstractmethod
    def inserir_documento(self, documento_entity: DocumentoEntity) -> DocumentoEntity:
        pass

    @abstractmethod
    def selecionar_documentos(self, filtro_entity: FiltroEntity) -> Optional[List[DocumentoEntity]]:
        pass

    @abstractmethod
    def criar_atualizar_tsv(self, documento_entity: DocumentoEntity) -> None:
        pass