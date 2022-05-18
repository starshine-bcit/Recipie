import string

def main_search(ingredients_list: list[str], categories: list[str], rlist: list[dict]) -> list[dict]:
    """
    This function checks if ingredients to search for are given or a list of categories was given
    if one of them are missing (eg. ingredients_list is empty), it will funnel the terms into their respective searches
    eg. (if only ingredients are given, uses exact search) (if only categories are given, uses category search)
    if both ingredients and categories are given, searches by category first, then ingredients.

    Use `e_search` to call the ingredients search functions
    or `category_search` to call the categories search function

    When we're done, this function should be transferrable between both esearch and psearch
    """

    if len(ingredients_list) == 0 and len(categories) != 0: 
        matched_recipes = category_search(categories, rlist)
    
    elif len(ingredients_list) != 0 and len(categories) == 0:
        matched_recipes = e_search(ingredients_list, rlist)
    
    elif len(ingredients_list)!= 0 and len(categories) != 0:
        diet_recipes = category_search(categories, rlist)
        matched_recipes = e_search(ingredients_list, diet_recipes)
    
    return matched_recipes 


############## You shouldn't need to touch anything after this line in the first iteration ################


def category_search(cat: list[str], rlist: list[dict]) -> list[dict]:
    """
    Searches through the recipe list(rlist) and returns recipes(dict) that match the category(s)(cat)
    """
    matched_recipe = []
    for recipe in rlist: 
        intersection = set(recipe["diets"]).intersection(set(cat)) 
        if len(intersection) == len(cat): 
            matched_recipe.append(recipe)

    return matched_recipe


################################ Exact Search Section ###############################################

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


def e_search(ingredient_input: list[str], recipes_list: list[dict]) -> list[dict]:
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

    for recipe in recipes_list: 
        match = 0
        ingred_list = []
        new_ingred_list = []
        exclude = ['soup', 'powder', 'puree', 'paste', 'sauce']

        if len(recipe['ingredients']) < 1 : continue # Remove after merging the latest Recipe commit
        # Removes an item from the exclude list if the user input an item
        for item in exclude:    
            for ui in user_input:
                if ui.find(item) != -1:
                    exclude.remove(item)

        total_ingredients = len(recipe['ingredients']) 
        for ingredients in recipe['ingredients']:
            ingred_list.append(ingredients)
        
        # Cleansing plurals in recipe's list of ingredients and turns it into one long string
        new_ingred_list = replace_chr(ingred_list)

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
            matched_recipe.append(recipe)

    return matched_recipe 

