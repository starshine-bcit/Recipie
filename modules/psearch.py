"""A function that takes in a list of ingredients and a list of recipes
and returns matching recipes (that use all ingredients) as a list"""

import re
from modules.recipe import Recipe
from modules.recipelist import RecipeList

# When testing, comment out above import blocks & uncomment below imports
# from ACIT2911.modules.recipe import Recipe
# from ACIT2911.modules.recipelist import RecipeList


def p_search(ingredients_list: list[str],
             recipes_list: RecipeList) -> list[Recipe]:
    """Finds recipes that contain all ingredients passed in.

    Args:
        ingredients_list (list[str]):
            List of string of ingredients that recipe should contain.
        recipes_list (list[Recipe]):
            List of Recipe instances.

    Returns:
        list[Recipe]:
            List of Recipe instances whose ingredients contain all
            ingredients (and possibly other ingredients) in ingredients_list.
    """

    # Number of ingredients needed to match
    required_matches = len(ingredients_list)

    # Cleaning ingredients input, remove plurals and make lowercase
    ingredients_list = [ingred.lower() for ingred in ingredients_list]
    ingredients_list = [remove_plural(ingred) for ingred in ingredients_list]

    matching_recipes = []

    # Iterate through recipes
    for recipe in recipes_list.recipes:
        # Start counting for ingredient matches in recipe
        matches = 0

        # Iterate through each input ingredient
        for ingredient in ingredients_list:
            # Iterate through each ingredient in recipe
            for rec_ingredient in recipe.ingredients:

                # Stop looping if number of matches is met
                if matches == required_matches:
                    break
                # Set up regex to look for possibly plural ingredient
                #  and commas and spaces to single out ingredient
                to_match = f'^{ingredient}[ies]*[,\\s]+|'\
                           f'[,\\s]+{ingredient}[ies]*$|'\
                           f'[,\\s]+{ingredient}[ies]*[,\\s]+|'\
                           f'^{ingredient}$'
                match = re.search(to_match, rec_ingredient)
                # Stop looping if input ingredient is in current
                #  recipe ingredient, increment if ingredients match
                if match:
                    matches += 1
                    break

            # Stop looping and add recipe to list to be returned
            #  if number of matches is met, move to next recipe
            if matches == required_matches:
                matching_recipes.append(recipe)
                break

    return matching_recipes


def remove_plural(ingredient: str) -> str:
    """Removes the end of words that are plural.

    Args:
        ingredient (str):
            The word to remove the plural ending from.

    Returns:
        str:
            Original word or word without plural ending
    """

    if ingredient.endswith('ies'):
        ingredient = ingredient.removesuffix('ies')
    elif ingredient.endswith('es'):
        ingredient = ingredient.removesuffix('es')
    elif ingredient.endswith('s'):
        ingredient = ingredient.removesuffix('s')
    return ingredient
