# Clean Code Example: Wood Crafting selling company

Clean code is a crucial aspect of software development. It ensures that your code is readable, maintainable, and adaptable. By following clean code principles, you can improve collaboration, reduce technical debt, and enhance the longevity of your projects. This repository aims to provide a practical example of clean code principles in action.

NOTE: The code and use cases here are oversimplified to make the reasoning behind the code easier to follow. But if you find any inconsistencies, feel free to open issues about it on github.

## Table of Contents

- [Business Need](#business-need)
- [Running The Code](#running-the-code)
- [Code Structure](#code-structure)
- [Entities](#entities)
- [Adapters](#adapters)
- [Use Cases](#use-cases)

## Business Need

The business need in this case is: creating wood tables to sell.

We will not worry about actually selling the tables or orders, just the creation of them. (this part might come later)

## Running The Code

To run the code, you'll need to simply run the python script in `src/main.py`.

Ideally you'd use the devcontainer extension in VSCode which will setup for you everything I defined in the `.devcontainer` forlder.

Otherwise:
* install manually the python dependencies running `pip install -r requirements.txt`
* run the script with `python src/main.py`

## Code Structure

The code is divided in the following 3 folders:
* adapters -> interfaces with the external world
* entities -> main entites of the app
* usecases -> business logic code

In the `main.py` file, we're using these 3 tools to achieve what our business needs. In more realistic scenarios you would instead expose this logic to other systems through APIs or similar.

### Entities

The enties constitute the *core entities* of our application, it's building blocks. All the codebase depends on these types, especially the business logic. Changes on these files should not be done lightly. (This is where type systems like MyPy come in very handy to ensure, as much as possible, that things don't break when they're changed)

In our case, the entities we need are:
* Table
* Wood

The separation between Wood and Table was made to allow for future possible extensions, like maybe doing shelves or other types of wood-based objects.

These types will ALWAYS be used as outputs of both the "adapters" and "usecases" functions, and might be used as inputs for the "usecases" functions (especially when re-using code from some usecases in other ones).

### Adapters

Adapters, as the *interfaces to the external world*, are in charge of taking the interface of all the code which is running outisde of our codebase and creating an internal, reusable, interface which abstracts away the actual call to the external resources.

In this example, we need 2 things from the outside world:
* something that extracts wood
* something that cuts wood

Maybe our company doesn't want to take care of these operations, or maybe it's another department doing so. The point is, it's not our code so we don't directly use it to achieve our business needs.

The same goes for the types, which I put in the respective `types.py` files. These types are not meant to be used from the rest of the codebase. These types exist only to allows us to use the external interfaces more confortably (type checking, validations, etc..) but once the data has been exchanged with these enternal resources, everything that the "adapters" functions return is using the types in the "entities" folder.

### Use Cases

Use Cases are where most of the actual business logic is performed.

In the "usecases" code, using the "adapters" to perform actions your code can't, or doesn't want to, do and using the "entities" as shared internal depenendencies to build on top of.

Currently, our business need is to "create wood tables", so we have only 1 file and it's called `tables.py` (it's called tables because the business is probably expanding later on to do other types of objects, which means grouping usecases per-object makes sense).

Inside the `tables.py` we have only one function: `make_wood_table`. This function excepts only to be told the "tint" of the table externally, and it returns a complete table as output.

The code in this folder NEVER directly speaks with the external world. If anything from the outside world is required to achieve the business logic, then an adapter needs to be made and only then it can be used from the "usecases" for what it's needed.