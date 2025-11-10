from dataclasses import asdict, is_dataclass
from typing import Any, Dict, List


def dataclass_to_dict(data: Any) -> Dict:

    if is_dataclass(data):
        return asdict(data)
    
    if isinstance(data, List):
        return [asdict(item) if is_dataclass(item) else item for item in data]
    
    return data