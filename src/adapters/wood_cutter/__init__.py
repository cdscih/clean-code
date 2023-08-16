from adapters.logger import Logger
from adapters.wood_cutter.types import CutWood as ExternalCutWood
from adapters.wood_cutter.types import SupportedShapes
from entities.wood import CutWood, Wood


def _cut_wood_using_knife(wood, shape: SupportedShapes) -> ExternalCutWood:
    return ExternalCutWood(shape=shape, lenght=10, height=10)


class WoodCutter:
    logger: Logger

    def __init__(self, logger: Logger):
        self.logger = logger

    def cut_wood(self, wood: Wood, shape: str) -> CutWood:
        self.logger.debug(f"Cutting wood: {wood}")

        try:
            supported_shape = SupportedShapes(shape)
        except ValueError as err:
            self.logger.error(f"Wood shape {shape} not supported.")
            raise err

        cut_wood = _cut_wood_using_knife(wood=wood, shape=supported_shape)
        self.logger.info(f"Cut wood: {cut_wood}")

        return CutWood(tint=wood.tint, shape=cut_wood.shape)
