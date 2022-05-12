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
    ingredient_list = []

    for ingredient in words_list:
        for word in ingredient.split(" "):
            word = word.lower().translate(str.maketrans('', '', string.punctuation))
            if word.endswith('ies'):
                word_list.append(word.replace('ies', 'y'))
            elif word.endswith('s'):
                word_list.append(word.removesuffix('s'))
            elif word.endswith('es'):
                word_list.append(word.removesuffix('es'))
            else: 
                word_list.append(word)
        ingredient_list.append(' '.join(word_list))
        word_list.clear()

    return ingredient_list 


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
        new_ingred_list = []
        exclude = ['soup', 'powder', 'puree', 'paste', 'sauce']

        if len(recipe.ingredients) < 1 : continue # Remove after merging the latest Recipe commit
        # Removes an item from the exclude list if the user input an item
        for item in exclude:    
            for ui in user_input:
                if ui.find(item) != -1:
                    exclude.remove(item)

        total_ingredients = len(recipe.ingredients) 
        for ingredients in recipe.ingredients:
            ingred_list.append(ingredients)
        
        # Cleansing plurals in recipe's list of ingredients and turns it into one long string
        new_ingred_list = replace_chr(ingred_list)

        for item in user_input:
            for ingred in new_ingred_list:
                if ingred.find(item) != -1:
                    for exclusion in exclude:
                        if ingred.find(exclusion) != -1:
                            break
                    else:
                        match += 1
                        break
    
        if match == total_ingredients: 
            matched_recipe.append(recipe)

    return matched_recipe 
