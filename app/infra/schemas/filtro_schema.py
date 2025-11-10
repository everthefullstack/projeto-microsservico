from pydantic import BaseModel, Field
from typing import Optional


class FiltroSchema(BaseModel):
    busca: str = Field(description="Termos da busca")
    latitude: Optional[float] = Field(default=None)
    longitude: Optional[float] = Field(default=None)