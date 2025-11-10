from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional
from app.domain.interfaces.documento_interface import DocumentoEntityInterface


@dataclass(slots=True, kw_only=True)
class DocumentoEntity(DocumentoEntityInterface):
    id: Optional[int] = field(default=None)
    titulo: str
    conteudo: str
    autor: str
    data: date
    latitude: float
    longitude: float

    def validar_titulo(self) -> bool:
        if not self.titulo:
            raise ValueError("Título não pode ser vazio.")
        
    def validar_conteudo(self) -> bool:
        if not self.conteudo:
            raise ValueError("Conteúdo não pode ser vazio.")

    def validar_autor(self) -> bool:
        if not self.autor:
            raise ValueError("Autor não pode ser vazio.")

    def validar_data(self) -> bool:
        try:
            self.data = datetime.strptime(self.data, "%Y-%m-%d").date()
            
        except ValueError:
            raise ValueError("Data inválida. Formato esperado: YYYY-MM-DD.")

    def validar_latitude(self) -> bool:
        if not self.latitude:
            raise ValueError("Latitude não pode ser vazia.")

    def validar_longitude(self) -> bool:
        if not self.longitude:
            raise ValueError("Longitude não pode ser vazia.")