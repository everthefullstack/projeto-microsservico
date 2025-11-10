from dataclasses import dataclass
from typing import List, Optional
from sqlmodel import Session, select, update, func
from app.application.interfaces.documento_interface import DocumentoRepositoryInterface
from app.domain.entities.documento_entity import DocumentoEntity
from app.domain.entities.filtro_entity import FiltroEntity
from app.infra.models.sqlmodel.documento_model import DocumentoModel
from app.presentation.adapters.documento_adapters import entity_to_model, model_to_entity
from app.infra.utils.calcular_latitude_longitude import calcular_latitude_longitude


@dataclass(slots=True, kw_only=True)
class DocumentoRepository(DocumentoRepositoryInterface):
    session: Optional[Session] = None

    def inserir_documento(self, documento_entity: DocumentoEntity) -> DocumentoEntity:
        documento_model: DocumentoModel = self.__entity_to_model(documento_entity)
        self.session.add(documento_model)
        self.session.flush()

        return self.__model_to_entity(documento_model)

    def selecionar_documentos(self, filtro_entity: FiltroEntity) -> Optional[List[DocumentoEntity]]:
        stmt = select(DocumentoModel).where(DocumentoModel.tsv.op("@@")(func.plainto_tsquery("portuguese", filtro_entity.busca)))

        documentos_model: List[DocumentoModel] | List = self.session.exec(statement=stmt)

        if filtro_entity.latitude and filtro_entity.longitude:
            documentos_model = sorted(
            documentos_model,
            key=lambda doc: calcular_latitude_longitude(
                filtro_entity.latitude, 
                filtro_entity.longitude,
                doc.latitude, 
                doc.longitude
            )
        )

        return [self.__model_to_entity(documento_model) for documento_model in documentos_model]
    
    def criar_atualizar_tsv(self, documento_entity: DocumentoEntity) -> None:
        stmt = (
            update(DocumentoModel)
            .values(tsv=func.to_tsvector('portuguese', func.concat(documento_entity.titulo, ' ', documento_entity.conteudo, ' ', documento_entity.autor)))
            .where(DocumentoModel.id == documento_entity.id)
        )
        
        resultado = self.session.exec(statement=stmt)
        self.session.flush()

        return True if resultado.rowcount > 0 else False
    
    def __entity_to_model(self, documento_entity: DocumentoEntity) -> DocumentoModel:
        return entity_to_model(documento_entity)
    
    def __model_to_entity(self, documento_model: DocumentoModel) -> DocumentoEntity:
        return model_to_entity(documento_model)
    
