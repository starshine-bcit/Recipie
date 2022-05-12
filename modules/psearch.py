# from .recipe import Recipe

"""A function that takes in a list of ingredients and a list of recipes
and returns matching recipes (that use all ingredients) as a list"""


def p_search(ingredients_list: list[str],
             recipes_list: list[dict]) -> list[dict]:
    """Finds recipes that contain all ingredients passed in.

    Args:
        ingredients_list (list[str]):
            List of string of ingredients that recipe should contain.
        recipes_list (list[dict]):
            List of dictionaries of recipes.

    Returns:
        list[dict]:
            List of dictionaries of recipes that contain all
            ingredients in ingredients_list.
    """

    required_matches = len(ingredients_list)
    ingredients_list = [ingred.lower() for ingred in ingredients_list]
    ingredients_list = [remove_plural(ingred) for ingred in ingredients_list]
    matching_recipes = []

    for recipe in recipes_list:
        matches = 0
        for rec_ingredient in recipe["ingredients"]:
            for ingredient in ingredients_list:
                if ingredient in rec_ingredient:
                    matches += 1
                if matches == required_matches:
                    break
            if matches == required_matches:
                matching_recipes.append(recipe)
                break
    # print(matching_recipes)
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
