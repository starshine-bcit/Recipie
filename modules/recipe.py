"""A module of a food recipe class."""

class Recipe:
    """A class that represents a food recipe.

    Attributes:
        name (str):
            Name of the recipe.
        ingredients (list[str]):
            Ingredients used in the recipe.
        instructions (str):
            Instructions for how to make the recipe.
    """

    def __init__(self, name: str, ingredients: list[str], instructions: str):
        if type(name) != str:
            raise TypeError(
                "Recipe name improperly formatted, should be string."
            )
        
        if type(ingredients) != list:
            raise TypeError(
                "Recipe ingredients improperly formatted, should be a list."
            )

        if type(instructions) != str:
            raise TypeError(
                "Recipe instructions improperly formatted, should be string."
            )

        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def to_dict(self) -> dict:
        """Returns dictionary of all Recipe attributes."""
        return self.__dict__
