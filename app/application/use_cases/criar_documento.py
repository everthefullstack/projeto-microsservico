from dataclasses import dataclass
from app.application.interfaces.documento_interface import CriarDocumentoUseCaseInterface
from app.application.interfaces.unit_of_work_interface import UnitOfWorkInterface
from app.domain.entities.documento_entity import DocumentoEntity


@dataclass(slots=True, kw_only=True)
class CriarDocumentoUseCase(CriarDocumentoUseCaseInterface):

    unit_of_work: UnitOfWorkInterface

    def criar_documento(self, documento_entity: DocumentoEntity) -> DocumentoEntity:
        with self.unit_of_work as uow:
            documento_entity.validar_titulo()
            documento_entity.validar_conteudo()
            documento_entity.validar_autor()
            documento_entity.validar_data()
            documento_entity.validar_latitude()
            documento_entity.validar_longitude()
            
            documento = uow.documento_repository.inserir_documento(documento_entity=documento_entity)
            resultado = uow.documento_repository.criar_atualizar_tsv(documento_entity=documento)

            if resultado:
                return documento
            
            raise ValueError("Erro ao criar o índice tsv no documento.")