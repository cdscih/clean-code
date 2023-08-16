from enum import Enum

from pydantic import BaseModel


class WoodTint(str, Enum):
    dark = "dark"
    light = "light"


class Wood(BaseModel):
    origin: str
    length: int
    height: int
    tint: WoodTint = WoodTint.dark


class CutWood(BaseModel):
    shape: str
    tint: WoodTint = WoodTint.dark
