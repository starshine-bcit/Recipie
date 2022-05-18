



def category_search(rlist: list[dict], cat: list[str]) -> list[dict]:
    """
    Searches through the recipe list(rlist) and returns recipes(dict) that match the category(s)(cat)
    """
    cor_recipes = []
    for recipe in rlist:
        for rlist['diet'] in recipe:
            if cat in rlist['diet']:
                cor_recipes.append[recipe]

   
