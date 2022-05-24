"""A function that takes a list of categories and a list of recipes,
returns a list of recipes that have the same category matches."""

from .recipe import Recipe
from .recipelist import RecipeList


def category_search(cat: list[str], rlist: RecipeList) -> list[Recipe]:
    """
    Takes a RecipeList (rlist) instance and compares the recipe instances categories if they match the categories (cat)

    Args:
        cat (list[str]): The list of categories that the users want filtered back to them
        rlist (RecipeList): The RecipeList instance, holds the recipes inside it

    Returns:
        list[Recipe]: A list of recipe instances
    """
    matched_recipe = []
    for recipe in rlist.recipes: 
        intersection = set(recipe.diets).intersection(set(cat))
        if len(intersection) == len(cat): 
            matched_recipe.append(recipe)

    return matched_recipe
