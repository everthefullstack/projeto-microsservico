from dataclasses import dataclass, field
from typing import Optional
from app.domain.interfaces.filtro_interface import FiltroInterface


@dataclass(slots=True, kw_only=True)
class FiltroEntity(FiltroInterface):
    busca: str
    latitude: Optional[float] = field(default=None)
    longitude: Optional[float] = field(default=None)

    def validar_buscar(self) -> bool:
        if not self.busca:
            raise ValueError("Busca não pode ser vazia.")
