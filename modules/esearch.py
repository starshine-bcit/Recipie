import string
from .recipe import Recipe
from .recipelist import RecipeList

def replace_chr(words_list:list[str]) -> list[str]:
    """
    Replaces plural form of words to their singular version

    Args:
        words_list (list[str]): List of a mix of plural/singular form words being transformed

    Returns:
        list[str]: list of singular form words
    """
    word_list = []
    for words in words_list: 
        word = words.lower().translate(str.maketrans(
            '', '', string.punctuation))
        if word.endswith('ies'):
            word_list.append(word.replace('ies', 'y'))
        elif word.endswith('s'):
            word_list.append(word.removesuffix('s'))
        elif word.endswith('es'):
            word_list.append(word.removesuffix('es'))
        else: 
            word_list.append(word)
    
    return word_list 


def exact_search(ingredient_input: list[str], recipes_list: RecipeList) -> list[Recipe]:
    """
    Searches through recipes that match the exact ingredients the user is looking for

    Args:
        ingredient_input (list[str]): The list of ingredients the user has given
        recipes_list (list[dict]): the list of recipes the search function will look through

    Returns:
        list[dict]: A list of recipes that matches what the user was looking for
    """
    matched_recipe = [] 
    # Cleansing plurals in list of ingredients user input 
    user_input = replace_chr(ingredient_input)

    for recipe in recipes_list.recipes: 
        match = 0
        ingred_list = [] 
        last_ingredient = ""
        exclude = ['soup', 'powder', 'puree', 'paste', 'sauce']

        # Removes an item from the exclude list if the user input an item
        for item in exclude:    
            for ui in user_input:
                if ui.find(item) >= 0:
                    exclude.remove(item)

        for ingredients in recipe.ingredients:
            for item in exclude:
                if item in ingredients: 
                    break   # Breaks the loop and skips the ingredient if it matches an item in the exclusion list
            else:
                ingred = ingredients.split(" ") # List of items  
                for i in ingred:
                    ingred_list.append(i)
        
        # Cleansing plurals in recipe's list of ingredients
        new_ingred_list = replace_chr(ingred_list)

        for ingredient in new_ingred_list:
            if ingredient in user_input:
                match += 1
            # Checks if a combination of the last ingredient + current ingredient matches the user input
            if f"{last_ingredient} {ingredient}" in user_input:
                match += 1
            last_ingredient = ingredient

        if match >= len(user_input): 
            matched_recipe.append(recipe)

    return matched_recipe 
