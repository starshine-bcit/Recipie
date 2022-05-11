from .recipe import Recipe
from .recipelist import RecipeList
import string


def exact_search(ingredient_input: list[str], recipes_list: RecipeList) -> list[Recipe]:
    matched_recipe = [] 
    user_input = [] 

    for user in ingredient_input: 
        user_ingred = user.lower()
        if user_ingred.endswith('ies'): 
            ingred_input = user_ingred.replace('ies', 'y')
            user_input.append(ingred_input)
            # user_input.append(user_ingred.replace('ies', 'y'))
        elif user.endswith('s'):
            ingred_input = user_ingred.replace('s', '')
            user_input.append(ingred_input)
            # user_input.append(user_ingred.replace('s', ''))
        elif user.endswith('es'):
            ingred_input = user_ingred.replace('es', '')
            user_input.append(ingred_input)
            # user_input.append(user_ingred.replace('es', ''))
        else: 
            user_input.append(user_ingred)

    for recipe in recipes_list.recipes: 
        match = True 
        new_ingred_list = [] 

        ingred_list = [i.lower().translate(str.maketrans(
            '', '', string.punctuation)) for i in recipe.ingredients]
            
        templist = []
        for ingredstring in ingred_list:
            for food in ingredstring.split(' '):
                if food.endswith('ies'): 
                    food_item = food.replace('ies', 'y')
                    # new_ingred_list.append(food.replace('ies', 'y'))
                elif food.endswith('s'):
                    food_item = food.replace('s', '')
                    # new_ingred_list.append(food.replace('s', ''))                     
                elif food.endswith('es'):
                    food_item = food.replace('es', '')
                    # new_ingred_list.append(food.replace('es', ''))
                else: 
                    food_item = food
                templist.append(food_item)
                
            new_ingred_list.append(templist)
            templist = []

        for ingred in new_ingred_list:
            ret = -1
            for term in user_input:
                fret = ingred.find(term)
                if fret > ret:
                    ret = fret
            if ret == -1:
                match = False
        if match is True:
            matched_recipe.append(recipe)

    return matched_recipe