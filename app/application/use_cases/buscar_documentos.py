from dataclasses import dataclass
from typing import List, Optional
from app.application.interfaces.documento_interface import BuscarDocumentoUseCaseInterface
from app.application.interfaces.unit_of_work_interface import UnitOfWorkInterface
from app.domain.entities.filtro_entity import FiltroEntity
from app.domain.entities.documento_entity import DocumentoEntity


@dataclass(slots=True, kw_only=True)
class BuscarDocumentoUseCase(BuscarDocumentoUseCaseInterface):

    unit_of_work: UnitOfWorkInterface

    def buscar_documentos(self, filtro_entity: FiltroEntity) -> Optional[List[DocumentoEntity]]:
        with self.unit_of_work as uow:
            documentos = uow.documento_repository.selecionar_documentos(filtro_entity=filtro_entity)

            if documentos:
                return documentos
            
            raise ValueError("Nenhum documento encontrado com os filtros fornecidos.")