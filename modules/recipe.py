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
            ingredients: list[str],
            instructions: str,
            diets: list[str]
        ):

        if type(id) != int:
            raise TypeError(
                "Recipe ID improperly formatted, should be an integer."
            )

        if type(name) != str:
            raise TypeError(
                "Recipe name improperly formatted, should be string."
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

        if type(diets) != list:
            raise TypeError(
                "Recipe diet labels improperly formatted, should be a list."
            )

        # Remove empty line ingredients
        ingredients = [ingred for ingred in ingredients if ingred != "\n"]

        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.diets = diets

    def to_dict(self) -> dict:
        """Returns dictionary of all Recipe attributes."""
        return self.__dict__

    def ingredients_as_str(self) -> str:
        """Returns ingredients in a list as string."""
        ingredients = '\n'.join(self.ingredients)
        return ingredients

    def add_label(self, label: str):
        """Appends dietary label to diets attribute.

        Args:
            label (str):
                Dietary label to add to the recipe.
        """
        self.diets.append(label)
