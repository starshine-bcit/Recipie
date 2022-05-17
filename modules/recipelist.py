"""Module of a class of a list of food recipes."""

import json
import random
from pathlib import Path
from .recipe import Recipe


class RecipeList:
    """Class represents a list of Recipe instances.
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

        # Numbering recipes for easy reference.
        count = 1

        for file in files:
            with file.open('r', encoding='utf-8') as fp:
                data = json.load(fp)

            for value in data:
                try:
                    self.recipes.append(
                        Recipe(
                            id = count,
                            name = value["name"],
                            diets = ['placeholder'],  #FIXME: update after diet labelling
                            ingredients = value["ingredients"],
                            instructions = value["instructions"]
                        )
                    )
                    count += 1
                except:
                    # Quick check of where it is breaking
                    # print(self.recipes[-1].name)
                    # Skip over non-recipes in JSON
                    continue

    def get_random_recipe(self) -> Recipe:
        """Returns a random Recipe from list of Recipes."""
        random_recipe = random.choice(self.recipes)
        return random_recipe

    # Method used when cleaning up multiple recipe data files.
    def save_recipes_to_file(self):
        """Writes recipes to JSON file"""
        with open("./data/recipe_list.json", "w") as fp:
            json.dump([rec.to_dict() for rec in self.recipes], fp)
