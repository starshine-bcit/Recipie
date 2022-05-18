



def category_search(rlist: list[dict], cat: list[str]) -> list[dict]:
    """
    Searches through the recipe list(rlist) and returns recipes(dict) that match the category(s)(cat)
    """
    matched_recipe = []
    for recipe in rlist: 
        intersection = set(recipe["diets"]).intersection(set(cat)) 
        if len(intersection) == len(cat): 
            matched_recipe.append(recipe)

    return matched_recipe
