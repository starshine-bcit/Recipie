"""A function that takes a list of ingredients and a list of recipes and returns matching recipes in a list
that have the same ingredients (if the recipe has ingredients that the user did not give, excludes them from the list)"""

import string
from .recipe import Recipe
from .recipelist import RecipeList
from .catsearch import category_search


def exact_search(ingredients_list: list[str], categories: list[str], rlist: RecipeList) -> list[Recipe]:
    """
    Filters searches based on whether it's given a mix of ingredients, categories, or both
    If the ingredients list is empty, funnels the search into `category_search`
    if the categories list is empty, funnels the search into `e_search`
    if both lists are filled, funnels the search into `category_search` before funneling it into `e_search`

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
        matched_recipes = e_search(ingredients_list, rlist)
    
    elif len(ingredients_list) != 0 and len(categories) != 0:
        diet_recipes = category_search(categories, rlist)
        matched_recipes = e_search(ingredients_list, diet_recipes)
    
    return matched_recipes


def replace_chr(words_list:list[str]) -> list[str]:
    """
    Replaces plural form of words to their singular version

    Args:
        words_list (list[str]): List of a mix of plural/singular form words being transformed

    Returns:
        list[str]: list of singular form words
    """
    word_list = []
    ingredient_list = []

    for ingredient in words_list:
        for word in ingredient.split(" "):
            word = word.lower().translate(str.maketrans('', '', string.punctuation))
            if word.endswith('ies'):
                word_list.append(word.removesuffix('ies'))
            elif word.endswith('y'):
                word_list.append(word.removesuffix('y'))
            elif word.endswith('s'):
                word_list.append(word.removesuffix('s'))
            elif word.endswith('es'):
                word_list.append(word.removesuffix('es'))
            else: 
                word_list.append(word)
        ingredient_list.append(' '.join(word_list))
        word_list.clear()

    return ingredient_list 


def recipe_match(user_input: list[str], recipe: Recipe) -> Recipe:
    match = 0
    ingred_list = []
    new_ingred_list = []
    exclude = ['soup', 'powder', 'puree', 'paste', 'sauce']

    # Removes an item from the exclude list if the user input an item
    for item in exclude:    
        for ui in user_input:
            if ui.find(item) != -1:
                exclude.remove(item)

    total_ingredients = len(recipe.ingredients) 
    for ingredients in recipe.ingredients:
        ingred_list.append(ingredients)
    
    # Cleansing plurals in recipe's list of ingredients and turns it into one long string
    new_ingred_list = ingred_list

    for ingred in new_ingred_list:
        for item in user_input:
            if ingred.find(item) != -1:
                for exclusion in exclude:
                    if ingred.find(exclusion) != -1:
                        break
                else:
                    match += 1
                    break

    if match == total_ingredients: 
        return recipe


def e_search(ingredient_input: list[str], recipes_list: RecipeList) -> list[Recipe]:
    """
    Searches through recipes that match the exact ingredients the user is looking for

    Args:
        ingredient_input (list[str]): The list of ingredients the user has given
        recipes_list (list[dict]): the list of recipes or a RecipeList instance that holds the recipes the search function will look through

    Returns:
        list[dict]: A list of recipes that matches what the user was looking for
    """
    matched_recipe = [] 
    # Cleansing plurals in list of ingredients user input 
    user_input = replace_chr(ingredient_input)
    print(user_input)

    if isinstance(recipes_list, list):
        for recipe in recipes_list: 
            result = recipe_match(user_input, recipe)
            if result == None:
                continue
            else:
                matched_recipe.append(result)

    if isinstance(recipes_list, RecipeList):
        for recipe in recipes_list.recipes: 
            result = recipe_match(user_input, recipe)
            if result == None:
                continue
            else:
                matched_recipe.append(result)

    return matched_recipe 
