from adapters import Adapters
from adapters.logger import Logger
from adapters.wood_extractor.types import SupportedTints
from entities.table import Leg, SupportedLegShapes, SupportedTopShapes, Top, WoodTable
from entities.wood import Wood


class Tables:
    logger: Logger
    adapters: Adapters

    def __init__(self, logger: Logger, config, adapters: Adapters):
        self.logger = logger
        self.config = config
        self.adapters = adapters

    def _get_wood_table_top(self, wood: Wood, shape="square") -> Top:
        cut_wood = self.adapters.wood_cutter.cut_wood(wood, shape=shape)

        try:
            top_shape = SupportedTopShapes(cut_wood.shape)
        except ValueError as err:
            self.logger.error(f"Top shape {cut_wood.shape} not supported.")
            raise err

        return Top(shape=top_shape)

    def _get_wood_table_legs(self, wood: Wood, shape="cylindrical", legs_n: int = 4) -> list[Leg]:
        legs: list[Leg] = []

        for _ in range(legs_n):
            cut_wood = self.adapters.wood_cutter.cut_wood(wood, shape=shape)
            try:
                leg_shape = SupportedLegShapes(cut_wood.shape)
            except ValueError as err:
                self.logger.error(f"Leg shape {cut_wood.shape} not supported.")
                raise err
            legs.append(Leg(shape=leg_shape))

        non_empty_created_legs = len(list(filter(lambda x: x is not None, legs)))

        if non_empty_created_legs != legs_n:
            raise Exception(
                f"Created legs count: {non_empty_created_legs} " f"doesn't match desired legs count: {legs_n}"
            )

        return legs

    def make_wood_table(self, tint: str) -> WoodTable:
        try:
            supported_tint = SupportedTints(tint)
        except ValueError as err:
            self.logger.error(f"Tint {tint} not supported.")
            raise err

        wood = self.adapters.wood_extractor.get_wood(tint=supported_tint)

        top = self._get_wood_table_top(wood=wood)
        legs = self._get_wood_table_legs(wood=wood)

        return WoodTable(top=top, legs=legs, tint=wood.tint)
