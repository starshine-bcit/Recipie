'''Module with constants for reference elsewhere'''

def get_basic_ingreds() -> list[str]:
    """
    Reads basic ingredients from csv file,
    returns sorted list of ingredients as lowercase string.
    """

    with open('./data/basic_ingredients.csv') as fp:
        data = fp.readlines()
    data = [line.lower().strip() for line in data]
    data.sort()
    return data

BASIC_INGRED = get_basic_ingreds()
