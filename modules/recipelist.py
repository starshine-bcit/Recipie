"""Module of a class of a list of food recipes."""

import json
from pathlib import Path
from .recipe import Recipe


class RecipeList:
    """Class represents a list of recipe instances.
    Recipes are from our recipe files.

    Args:
        files (list[Path]):
            List of Path instances of all recipe JSON files.

    Attributes:
        recipes (list[Recipe]):
            List of recipes as Recipe instances.
    """

    def __init__(self, files: list[Path]):
        self.recipes = []

        for file in files:
            with file.open('r', encoding='utf-8') as fp:
                data = json.load(fp)

            for value in data.values():
                try:
                    self.recipes.append(
                        Recipe(
                            name = value["title"],
                            ingredients = value["ingredients"],
                            instructions = value["instructions"]
                        )
                    )
                except:
                    # Quick check of where it is breaking
                    # print(self.recipes[-1].name)
                    # Skip over non-recipes in JSON
                    continue
