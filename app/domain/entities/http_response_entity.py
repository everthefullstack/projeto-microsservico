from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(slots=True, kw_only=True)
class HttpResponseEntity:

    status_code: int
    message: Optional[str] = None
    body: Dict
    