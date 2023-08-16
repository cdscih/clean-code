from adapters import Adapters
from usecases.tables import Tables


class UseCases:
    tables: Tables

    def __init__(self, config, adapters: Adapters):
        self.tables = Tables(logger=adapters.logger, config=config, adapters=adapters)
