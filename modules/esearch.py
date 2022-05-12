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
    processed_ingredient = False
    matched_recipe = [] 
    user_input = replace_chr(ingredient_input) # Cleansing plurals in list of ingredients user input 
    for ui in user_input:   #Checks if user input more than one word, most likely to be a processed ingredient??????
        if len(ui.split(" ")) == 2:
            processed_ingredient = True

    for recipe in recipes_list: 
        match = 0
        ingred_list = [] 
        exclude = ['soup', 'powder', 'puree', 'paste', 'sauce']
        for item in exclude:    # Removes an item from the exclude list if the user input an item
            for ui in user_input:
                if ui.find(item) >= 0:
                    exclude.remove(item)

        for ingredients in recipe["ingredients"]:
            for item in exclude:
                if item in ingredients: 
                    break   #Breaks the loop and skips the ingredient if it matches an item in the exclusion list
            else:
                ingred = ingredients.split(" ") # List of items  
                for i in ingred:
                    ingred_list.append(i)
        
        new_ingred_list = replace_chr(ingred_list) # Cleansing plurals in recipe's list of ingredients

        if processed_ingredient:
            last_ingredient = ""

            for ingredient in new_ingred_list:
                if ingredient in user_input:
                    match += 1
                if str(last_ingredient + " " + ingredient) in user_input:   #Checks if a combination of the last ingredient + current ingredient matches the user input
                    match += 1
                last_ingredient = ingredient
        else:
            for ui in user_input:
                if ui in new_ingred_list:
                    match += 1

        if match >= len(user_input): 
            matched_recipe.append(recipe)

    return matched_recipe 
