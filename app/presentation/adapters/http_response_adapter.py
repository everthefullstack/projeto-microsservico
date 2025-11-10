from app.domain.entities.http_response_entity import HttpResponseEntity
from typing import Dict


def entity_to_response(status_code: int, message: str, data: Dict) -> HttpResponseEntity:

    return HttpResponseEntity(
        status_code=status_code,
        message=message,
        body=data
    )
