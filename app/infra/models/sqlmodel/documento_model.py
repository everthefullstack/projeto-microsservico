from sqlmodel import SQLModel, Field, Column
from sqlalchemy.dialects.postgresql import TSVECTOR
from datetime import date
from typing import Optional


class DocumentoModel(SQLModel, table=True):
    __tablename__ = 'tb_documento'

    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str = Field(nullable=False)
    conteudo: str = Field(nullable=False)
    autor: str = Field(nullable=False)
    data: date = Field(nullable=False)
    latitude: float = Field(nullable=False)
    longitude: float = Field(nullable=False)
    tsv: Optional[str] = Field(sa_column=Column(TSVECTOR))