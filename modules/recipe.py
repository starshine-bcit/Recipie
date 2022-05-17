"""A module of a food recipe class."""

class Recipe:
    """A class that represents a food recipe.

    Attributes:
        id (int):
            ID number of recipe when in a list.
        name (str):
            Name of the recipe.
        diets (list[str]):
            Dietary labels/categories of the recipe.
        ingredients (list[str]):
            Ingredients used in the recipe.
        instructions (str):
            Instructions for how to make the recipe.
    """

    def __init__(
            self,
            id: int,
            name: str,
            diets: list[str],
            ingredients: list[str],
            instructions: str
        ):

        if type(id) != int:
            raise TypeError(
                "Recipe ID improperly formatted, should be an integer."
            )

        if type(name) != str:
            raise TypeError(
                "Recipe name improperly formatted, should be string."
            )

        if type(diets) != list:
            raise TypeError(
                "Recipe diet labels improperly formatted, should be a list."
            )
        
        for label in diets:
            if type(label) != str:
                raise TypeError(
                    "Recipe diet label should be string."
                )

        if type(ingredients) != list:
            raise TypeError(
                "Recipe ingredients improperly formatted, should be a list."
            )

        for ingred in ingredients:
            if type(ingred) != str:
                raise TypeError(
                    "Each ingredient in recipe should be string."
                )

        if type(instructions) != str:
            raise TypeError(
                "Recipe instructions improperly formatted, should be string."
            )

        self.id = id
        self.name = name
        self.diets = diets
        self.ingredients = ingredients
        self.instructions = instructions

    def to_dict(self) -> dict:
        """Returns dictionary of all Recipe attributes."""
        return self.__dict__

    def ingredients_as_str(self) -> str:
        """Returns ingredients in a list as string."""
        ingredients = '\n'.join(self.ingredients)
        return ingredients
