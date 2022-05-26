"""Module of a class of a list of food recipes."""

import json
import random
from pathlib import Path

from .recipe import Recipe


# Import below when json data does not have dietary labels
# from .constants import GLUTEN_FREE, LACTOSE_FREE, NUT_FREE, VEGAN, VEGGIE


class RecipeList:
    """Class represents a list of Recipe instances.
    Recipes are from our recipe files.

    Args:
        files (list[Path]):
            List of Path instances of all recipe JSON files.
        callback (ProgressCallback):
            Instance of a ProgressCallback Qobject from revent to emit signals.

    Attributes:
        recipes (list[Recipe]):
            List of recipes as Recipe instances.
    """

    def __init__(self, files: list[Path], callback):
        self.recipes = []
        data = {}

        for file in files:
            with file.open('r', encoding='utf-8') as fp:
                data.update(json.load(fp))

        count = 0  # Init counter for signals to 0
        tlen = len(data)  # Set total length to calc % done
        for key, value in data.items():
            try:
                self.recipes.append(
                    Recipe(
                        id=int(key),
                        # id=int(key),  # Use when json does not have id
                        name=value["title"],
                        ingredients=value["ingreds"],
                        instructions=value["instruct"],
                        diets=value["cat"],  # Use when json has dietary labels
                        # diets=[]  # Use when json does not have dietary labels
                    )
                )
                if count % 100 == 0: # So we don't send signals every nanosecond
                    callback(int(count/tlen*100))  # Send signal in % done
                count += 1 # increment count on each iter
            except:
                # Catches any errors from Recipe instantiation and
                #  skips over non-recipes in JSON.
                continue

        # Run below if recipes need dietary labels.
        # self.vegetarian = self.add_diet_labels('vegetarian', VEGGIE)
        # self.vegan = self.add_diet_labels('vegan', VEGAN)
        # self.gluten_free = self.add_diet_labels('glutenfree', GLUTEN_FREE)
        # self.nut_free = self.add_diet_labels('nutfree', NUT_FREE)
        # self.lactose_free = self.add_diet_labels('lactosefree', LACTOSE_FREE)

    def get_random_recipe(self) -> Recipe:
        """Returns a random Recipe from list of Recipes."""
        random_recipe = random.choice(self.recipes)
        return random_recipe

    # This method was used when cleaning up recipe data files.
    def save_recipes_to_file(self, count, filepath: str) -> int:
        """Writes recipes to JSON file

        Args:
            count (int):
                Number for continuous numbering of all recipes.
            filepath (str):
                Relative path to new file to write into.
        """

        recipes_json = {}

        with open(filepath, "w", encoding='utf-8') as fp:
            for recipe in self.recipes:
                recipes_json.update(
                    {recipe.id: {
                        "title": recipe.name,
                        "ingreds": recipe.ingredients,
                        "instruct": recipe.instructions,
                        "cat": recipe.diets
                    }}
                )
                count += 1
            json.dump(recipes_json, fp, indent=4)
            print(count)  # Use to know number of recipes written (verbosity)
        return count

    # Adds dietary label to recipe and returns list of recipes.
    def add_diet_labels(
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

            # Combine all ingredients into one lowercase string.
            rec_ingreds = recipe.ingredients_as_str().lower()

            for ingred in exclude_ingreds:

                # Skip to next recipe if an exlusion ingredient
                #  is in the recipe ingredients.
                if ingred in rec_ingreds:
                    break

                # If last exclude ingredient is reached without
                #  breaking loop and label is not already in the
                #  recipe, the recipe is labeled and appended.
                if ingred == exclude_ingreds[-1] and label not in recipe.diets:
                    recipe.add_label(label)
                    results_list.append(recipe)

        return results_list
