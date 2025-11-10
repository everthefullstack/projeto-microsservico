from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import JSONResponse, Response
from typing import Annotated
from app.presentation.adapters.http_request_adapter import request_to_entity
from app.presentation.composers.documento.buscar_documento_composer import BuscarDocumentosControllerComposer
from app.presentation.composers.documento.criar_documento_composer import CriarDocumentoControllerComposer
from app.infra.schemas.filtro_schema import FiltroSchema
from app.infra.schemas.documento_schema import DocumentoSchema


documento_routes = APIRouter(tags=["Documento"], prefix="/documentos")

@documento_routes.get("/", status_code=200)
async def buscar_documentos(request: Request, req: Annotated[FiltroSchema, Query()]):

    controller = BuscarDocumentosControllerComposer.compose()
    http_request_entity = await request_to_entity(request=request)
    http_response_entity = controller.buscar_documentos(http_request_entity=http_request_entity)

    if http_response_entity.status_code == 200:
        return JSONResponse(status_code=http_response_entity.status_code, 
                            content=http_response_entity.body)
    
    raise HTTPException(status_code=http_response_entity.status_code, 
                        detail=http_response_entity.body)


@documento_routes.post("/", status_code=201)
async def criar_documento(request: Request, req: DocumentoSchema):

    controller = CriarDocumentoControllerComposer.compose()
    http_request_entity = await request_to_entity(request=request)
    http_response_entity = controller.criar_documento(http_request_entity=http_request_entity)

    if http_response_entity.status_code == 201:
        return JSONResponse(status_code=http_response_entity.status_code, 
                            content=http_response_entity.body)
    
    raise HTTPException(status_code=http_response_entity.status_code, 
                        detail=http_response_entity.body)