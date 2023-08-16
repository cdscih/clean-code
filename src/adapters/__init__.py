from adapters.logger import Logger
from adapters.wood_cutter import WoodCutter
from adapters.wood_extractor import WoodExtractor


class Adapters:
    wood_extractor: WoodExtractor
    wood_cutter: WoodCutter

    def __init__(self):
        self.logger = Logger()
        self.wood_extractor = WoodExtractor(self.logger)
        self.wood_cutter = WoodCutter(self.logger)
