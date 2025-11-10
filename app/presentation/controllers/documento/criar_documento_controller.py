from dataclasses import dataclass
from app.application.interfaces.documento_interface import CriarDocumentoUseCaseInterface
from app.domain.entities.http_request_entity import HttpRequestEntity
from app.domain.entities.http_response_entity import HttpResponseEntity
from app.domain.entities.documento_entity import DocumentoEntity
from app.presentation.adapters.dataclass_adapter import dataclass_to_dict


@dataclass(slots=True)
class CriarDocumentoController:

    criar_documento_use_case: CriarDocumentoUseCaseInterface

    def criar_documento(self, http_request_entity: HttpRequestEntity) -> HttpResponseEntity:
        
        documento_entity: DocumentoEntity = DocumentoEntity(
            titulo=http_request_entity.body.get("titulo"),
            conteudo=http_request_entity.body.get("conteudo"),
            autor=http_request_entity.body.get("autor"),
            data=http_request_entity.body.get("data"),
            latitude=http_request_entity.body.get("latitude"),
            longitude=http_request_entity.body.get("longitude")
        )
        documento_response = self.criar_documento_use_case.criar_documento(documento_entity=documento_entity)

        return HttpResponseEntity(status_code=201, body=dataclass_to_dict(documento_response))
    