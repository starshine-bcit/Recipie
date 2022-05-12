# from .recipe import Recipe

"""A function that takes in a list of ingredients and a list of recipes
and returns matching recipes (that use all ingredients) as a list"""



def p_search(ingredients_list: list[str], recipes_list: list[dict]) -> list[dict]:
        matched = []
        for recipe in recipes_list:
            for sentence in recipe['ingredients']:
                all_word = sentence.split()
            if (any(n in ingredients_list for n in all_word)) == True:
                matched.append(recipe)    
        return(matched)   
    
