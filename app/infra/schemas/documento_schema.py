from pydantic import BaseModel, Field
from datetime import date


class DocumentoSchema(BaseModel):
    titulo: str = Field(description="Título do documento")
    conteudo: str = Field(description="Conteúdo do documento")
    autor: str = Field(description="Autor do documento")
    data: date = Field(description="Data do documento no formato YYYY-MM-DD")
    latitude: float = Field(description="Latitude da localização do documento")
    longitude: float = Field(description="Longitude da localização do documento")
