from ACIT2911.modules.recipelist import RecipeList

def exact_search(ingredient_input: list[str], recipes_list: list[dict]) -> list[dict]:
    matched = []
    user_input = [] 
    for user in ingredient_input: 
        user_ingredient = user.lower()
        user_input.append(user_ingredient)

    for recipe in recipes_list: 
        match = True 
        for ingredients in recipe["ingredients"]:
            ingred = ingredients.split(" ")
            if ingred[-1] not in user_input:
                match = False
        if match is True: 
            matched.append(recipe)
                    
    return matched 
