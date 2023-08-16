from enum import Enum

from pydantic import BaseModel


class SupportedShapes(str, Enum):
    SQUARE = "square"
    HEXAGONAL = "hexagonal"
    CYLINDRICAL = "cylindrical"


class CutWood(BaseModel):
    shape: SupportedShapes
    lenght: int
    height: int
