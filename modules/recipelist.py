"""Module of a class of a list of food recipes."""

import json
import random
from pathlib import Path
from .recipe import Recipe
from .constants import GLUTEN_FREE, LACTOSE_FREE, NUT_FREE, VEGAN, VEGGIE


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
                count = 0

            for key, value in data.items():
                try:
                    self.recipes.append(
                        # FIXME: change un/commented code when done with data
                        Recipe(
                            id = count,
                            # id = int(key),
                            name = value["title"],
                            # ingredients = value["ingreds"],
                            ingredients = value["ingredients"],
                            # instructions = value["instruct"],
                            instructions = value["instructions"],
                            # diets = ["cat"], #  for when json has diets
                            diets = []  #  placeholder
                        )
                    )
                    count += 1
                except:
                    # Quick check of where it is breaking
                    # print(self.recipes[-1].name)
                    # Skip over non-recipes in JSON
                    continue
        
        # FIXME: recipes for different diets
        # self.not_pie = self.get_diet_recipes('not a pie', ['apples', 'blueberries'])
        self.vegetarian = self.get_diet_recipes('vegetarian', VEGGIE)
        self.vegan = self.get_diet_recipes('vegan', VEGAN)
        self.gluten_free = self.get_diet_recipes('glutenfree', GLUTEN_FREE)
        self.nut_free = self.get_diet_recipes('nutfree', NUT_FREE)
        self.lactose_free = self.get_diet_recipes('lactosefree', LACTOSE_FREE)

    def get_random_recipe(self) -> Recipe:
        """Returns a random Recipe from list of Recipes."""
        random_recipe = random.choice(self.recipes)
        return random_recipe

    # Method used when cleaning up recipe data files.
    # Can be deleted when recipes are clean.
    def save_recipes_to_file(self, count, filepath: str):
        """Writes recipes to JSON file

        Args:
            count (int):
                Number for continuous numbering of all recipes.
            filepath (str):
                Relative path to new file to write into.
        """

        recipes_json = {}
        # ar, epi, fn
        # count = 0
        # count = 39522
        # count = 64845
        # count = 124473
        with open(filepath, "w") as fp:
            for recipe in self.recipes:
                recipes_json.update(
                    {count: {
                        "title": recipe.name,
                        "ingreds": recipe.ingredients,
                        "instruct": recipe.instructions,
                        "cat": recipe.diets
                    }}
                )
                count +=1
            json.dump(recipes_json, fp, indent = 4)
            print(count)
        return count

    # Adds dietary label to recipe and returns list of recipes
    def get_diet_recipes(
        self,
        label: str,
        exclude_ingreds: list[str]
    ) -> list[Recipe]:
        """Adds dietary label to appropriate recipes, returns recipes.

        Args:
            label (str):
                Dietary label to add to the recipe.
            exclude_ingreds (list[str]):
                Ingredients that are not part of the diet.

        Returns:
            list[Recipe]:
                Recipes that fit the dietary label.
        """

        results_list = []
        for recipe in self.recipes:

            # Combine all ingredients into one string.
            rec_ingreds = recipe.ingredients_as_str()

            for ingred in exclude_ingreds:
                
                # Skip to next recipe if an exlusion ingredient 
                #  is in the recipe ingredients.
                if ingred in rec_ingreds:
                    break
                
                # If last exclude ingredient is reached without
                #  breaking loop, recipe is labeled and appended.
                if ingred == exclude_ingreds[-1]:
                    recipe.add_label(label)  #FIXME: remove labelling later
                    results_list.append(recipe)

        return results_list
