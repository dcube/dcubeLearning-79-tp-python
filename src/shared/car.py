''' ** '''

from dataclasses import dataclass, field
import json
from typing import Dict


@dataclass
class Car:
    ''' Ma class Voiture '''

    color: str
    size: int
    properties: Dict[str, str]

    secret: str = field(init=False, repr=False, default='')

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)
