from enum import Enum
from typing import Optional

from pydantic import BaseModel


class SupportedShapes(str, Enum):
    square = "square"
    hexagonal = "hexagonal"
    cylindrical = "cylindrical"


class SupportedTints(str, Enum):
    dark = "dark"
    light = "light"
    really_dark = "really_dark"


class Wood(BaseModel):
    length: int
    height: int
    origin: Optional[str]
    age: Optional[int]
    tint: SupportedTints = SupportedTints.dark
    shape: SupportedShapes = SupportedShapes.square
