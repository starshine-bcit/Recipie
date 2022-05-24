"""A function that takes a list of categories and a list of recipes,
returns a list of recipes that have the same category matches."""

import string
from .recipe import Recipe
from .recipelist import RecipeList


def category_search(cat: list[str], rlist: RecipeList) -> list[Recipe]:
    """
    Searches through the recipe list(rlist) and returns recipes(dict) that match the category(s)(cat)
    """
    matched_recipe = []
    for recipe in rlist.recipes: 
        intersection = set(recipe.diets).intersection(set(cat))
        if len(intersection) == len(cat): 
            matched_recipe.append(recipe)

    return matched_recipe
