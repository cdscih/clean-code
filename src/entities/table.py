from enum import Enum

from pydantic import BaseModel

from entities.wood import WoodTint


class SupportedTopShapes(str, Enum):
    square = "square"
    hexagonal = "hexagonal"


class Top(BaseModel):
    shape: SupportedTopShapes = SupportedTopShapes.square


class SupportedLegShapes(str, Enum):
    cylindrical = "cylindrical"
    square = "square"


class Leg(BaseModel):
    shape: SupportedLegShapes = SupportedLegShapes.cylindrical


class Table(BaseModel):
    tint: str
    top: Top
    legs: list[Leg]


class WoodTable(Table):
    tint: WoodTint
