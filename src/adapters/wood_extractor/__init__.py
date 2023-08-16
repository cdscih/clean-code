from adapters.logger import Logger
from adapters.wood_extractor.types import SupportedTints
from adapters.wood_extractor.types import Wood as ExternalWood
from entities.wood import Wood, WoodTint


def _get_wood_from_forest(tint: SupportedTints) -> ExternalWood:
    return ExternalWood(tint=tint, length=100, height=100, origin="IT", age=50)


class WoodExtractor:
    logger: Logger

    def __init__(self, logger: Logger):
        self.logger = logger

    def get_wood(self, tint: SupportedTints) -> Wood:
        forest_wood = _get_wood_from_forest(tint)
        self.logger.info(f"Extracted wood from forest: {forest_wood}")
        try:
            wood_tint = WoodTint(forest_wood.tint)
        except ValueError as err:
            self.logger.error(f"Tint {forest_wood.tint} not supported.")
            raise err
        return Wood(
            origin="forest",
            length=forest_wood.length,
            height=forest_wood.height,
            tint=wood_tint,
        )
