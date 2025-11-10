from app.domain.entities.documento_entity import DocumentoEntity
from app.infra.models.sqlmodel.documento_model import DocumentoModel
from datetime import date


def entity_to_model(documento_entity: DocumentoEntity) -> DocumentoModel:
    return DocumentoModel(
        titulo=documento_entity.titulo,
        conteudo=documento_entity.conteudo,
        autor=documento_entity.autor,
        data=documento_entity.data,
        latitude=documento_entity.latitude,
        longitude=documento_entity.longitude,
    )

def model_to_entity(documento_model: DocumentoModel) -> DocumentoEntity:
    return DocumentoEntity(
        id=documento_model.id,
        titulo=documento_model.titulo,
        conteudo=documento_model.conteudo,
        autor=documento_model.autor,
        data=date.isoformat(documento_model.data),
        latitude=documento_model.latitude,
        longitude=documento_model.longitude,
    )
