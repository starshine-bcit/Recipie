
def exact_search(ingredient_input: list[str], recipes_list: list[dict]) -> list[dict]:
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

    for recipe in recipes_list: 
        match = True 
        ingred_list = [] 
        new_ingred_list = [] 

        for ingredients in recipe["ingredients"]:
            ingred = ingredients.split(" ") # List of items  
            ingred_list.append(ingred[-1]) # Append last word of a string 
            
        for food in ingred_list:
            if food.endswith('ies'): 
                food_item = food.replace('ies', 'y')
                new_ingred_list.append(food_item)
                # new_ingred_list.append(food.replace('ies', 'y'))
            elif food.endswith('s'):
                food_item = food.replace('s', '')
                new_ingred_list.append(food_item)
                # new_ingred_list.append(food.replace('s', ''))                     
            elif food.endswith('es'):
                food_item = food.replace('es', '')
                new_ingred_list.append(food_item)
                # new_ingred_list.append(food.replace('es', ''))
            else: 
                new_ingred_list.append(food)

        for new_food in new_ingred_list: 
            if new_food not in user_input:
                match = False

        if match is True: 
            matched_recipe.append(recipe)

    return matched_recipe 
