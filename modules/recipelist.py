"""Module of a class of a list of food recipes."""

from dis import Instruction
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

        for file in files:
            with file.open('r', encoding='utf-8') as fp:
                data = json.load(fp)

            for key, value in data.items():
                try:
                    self.recipes.append(
                        Recipe(
                            id = int(key),
                            name = value["title"],
                            ingredients = value["ingreds"],
                            instructions = value["instruct"],
                            diets = ['placeholder']
                        )
                    )
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
        recipes_json = {}
        count = 0
        with open("./data/recipe_list_test_test.json", "w") as fp:
            for recipe in self.recipes:
                recipes_json.update(
                    {count: {
                        "title": recipe.name,
                        "ingreds": recipe.ingredients,
                        "instruct": recipe.instructions,
                        "cat": []
                    }}
                )
                count +=1
            json.dump(recipes_json, fp, indent = 4)


    # WORK IN PROGRESS
    # Get list of recipes that belong to diet
    # def add_diet_recipes(
    #         self,
    #         label: str,
    #         exclude_ingreds: list[str]
    # ) -> list[Recipe]:

    #     results_list = []
    #     for recipe in self.recipes:
    #         rec_ingreds = recipe.ingredients_as_str()
    #         matches = 0
    #         for ingred in exclude_ingreds:
    #             if ingred in rec_ingreds:
    #                 break
    #             if ingred == exclude_ingreds[-1]:
    #                 recipe.diets.append(f'{label}')
    #                 results_list.append(recipe)
    #     return results_list

    # # Pass above return into below fnx

    # # Add label to diet recipes
    # def add_diet_label(self, label, diet_recipes: list[Recipe]):
    #     for d_rec in diet_recipes:
    #         pass
