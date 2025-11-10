from dataclasses import dataclass
from app.application.interfaces.documento_interface import BuscarDocumentoUseCaseInterface
from app.domain.entities.http_request_entity import HttpRequestEntity
from app.domain.entities.http_response_entity import HttpResponseEntity
from app.domain.entities.filtro_entity import FiltroEntity
from app.presentation.adapters.dataclass_adapter import dataclass_to_dict


@dataclass(slots=True)
class BuscarDocumentosController:

    buscar_documentos_use_case: BuscarDocumentoUseCaseInterface

    def buscar_documentos(self, http_request_entity: HttpRequestEntity) -> HttpResponseEntity:
        filtro_entity: FiltroEntity = FiltroEntity(
            busca=http_request_entity.query_params.get("busca"),
            latitude=http_request_entity.query_params.get("latitude"),
            longitude=http_request_entity.query_params.get("longitude")
        )

        documentos_response = self.buscar_documentos_use_case.buscar_documentos(filtro_entity=filtro_entity)

        return HttpResponseEntity(status_code=200, body=dataclass_to_dict(documentos_response))
