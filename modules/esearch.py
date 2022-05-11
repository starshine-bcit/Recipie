def replace_chr(words_list:list[str]) -> list[str]:
    word_list = []
    for words in words_list: 
        word = words.lower()
        if word.endswith('ies'):
            word_list.append(word.replace('ies', 'y'))
        elif word.endswith('s'):
            word_list.append(word.replace('s', ''))
        elif word.endswith('es'):
            word_list.append(word.replace('es', ''))
        else: 
            word_list.append(word)
    
    return word_list 
        

def exact_search(ingredient_input: list[str], recipes_list: list[dict]) -> list[dict]:
    matched_recipe = [] 
    user_input = replace_chr(ingredient_input) # List of ingredients user input 

    for recipe in recipes_list: 
        match = True 
        ingred_list = [] 

        for ingredients in recipe["ingredients"]:
            ingred = ingredients.split(" ") # List of items  
            ingred_list.append(ingred[-1]) # Append last word of a string 
        
        new_ingred_list = replace_chr(ingred_list)

        for new_food in new_ingred_list: 
            if new_food not in user_input:
                match = False

        if match is True: 
            matched_recipe.append(recipe)

    return matched_recipe 
