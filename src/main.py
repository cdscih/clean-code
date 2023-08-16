from adapters import Adapters
from usecases import UseCases

adapters = Adapters()
usecases = UseCases(adapters=adapters, config=None)

table = usecases.tables.make_wood_table(tint="dark")


print("\n" + "Created Table: \n" + table.model_dump_json(indent=4))
