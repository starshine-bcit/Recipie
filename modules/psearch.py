"""A function that takes in a list of ingredients and a list of recipes
and returns matching recipes (that use all ingredients) as a list"""

# import re
from modules.recipe import Recipe
from modules.recipelist import RecipeList

# When testing, comment out above import blocks & uncomment below imports
# from ACIT2911.modules.recipe import Recipe
# from ACIT2911.modules.recipelist import RecipeList


def partial_search(ingredients_list: list[str], categories: list[str], rlist: RecipeList) -> list[Recipe]:
    """
    Filters searches based on whether it's given a mix of ingredients, categories, or both
    If the ingredients list is empty, funnels the search into `category_search`
    if the categories list is empty, funnels the search into `p_search`
    if both lists are filled, funnels the search into `category_search` before funneling it into `p_search`

    Args:
        ingredients_list (list[str]): The list of ingredients the user gives
        categories (list[str]): the list of categories being given
        rlist (RecipeList): The RecipeList instance

    Returns:
        list[Recipe]: The list of Recipe instances that match the search terms given
    """
    if len(ingredients_list) == 0 and len(categories) != 0: 
        matched_recipes = category_search(categories, rlist)
    
    elif len(ingredients_list) != 0 and len(categories) == 0:
        matched_recipes = p_search(ingredients_list, rlist)
    
    elif len(ingredients_list) != 0 and len(categories) != 0:
        diet_recipes = category_search(categories, rlist)
        matched_recipes = p_search(ingredients_list, diet_recipes)
    
    return matched_recipes


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


def recipe_match(ingredients_list: list[str], recipe: Recipe) -> Recipe:
    """
    Is given a list of ingredients and single Recipe, returns the recipe if it matches the ingredients or none if it does not match

    Args:
        ingredients_list (list[str]): The list of ingredients the function will compare against the recipe ingredients
        recipe (Recipe): The recipe that is checked

    Returns:
        Recipe or None: The recipe that is returned if it matches, None is returned if there are no matches 
    """
    required_matches = len(ingredients_list)
    matches = 0

    for ingredient in ingredients_list:
        # Iterate through each ingredient in recipe
        for rec_ingredient in recipe.ingredients:

            # Stop looping if number of matches is met
            if matches == required_matches:
                break
            
            # Stop looping if input ingredient is in current
            #  recipe ingredient, increment if ingredients match
            if ingredient in rec_ingredient:
                matches += 1
                break   

            ### Regex to be explored another time.
            # # Set up regex to look for possibly plural ingredient
            # #  and commas and spaces to single out ingredient
            # to_match = f'^{ingredient}[ies]*[,\\s]+|'\
            #         f'[,\\s]+{ingredient}[ies]*$|'\
            #         f'[,\\s]+{ingredient}[ies]*[,\\s]+|'\
            #         f'^{ingredient}$'
            # match = re.search(to_match, rec_ingredient)
            # # Stop looping if input ingredient is in current
            # #  recipe ingredient, increment if ingredients match
            # if match:
            #     matches += 1
            #     break
            ###

        # Stop looping and add recipe to list to be returned
        #  if number of matches is met, return recipe
        if matches == required_matches:
            return recipe
                    


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


    if isinstance(recipes_list, list):
        for recipe in recipes_list:
            result = recipe_match(ingredients_list, recipe)
            if result == None:
                continue
            else:
                matching_recipes.append(result)


    if isinstance(recipes_list, RecipeList):
        for recipe in recipes_list.recipes:
            result = recipe_match(ingredients_list, recipe)
            if result == None:
                continue
            else:
                matching_recipes.append(result)
    
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
