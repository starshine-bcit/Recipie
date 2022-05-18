'''Module with constants for reference elsewhere'''

BASIC_INGREDS = ['baking', 'barbeque sauce', 'basil', 'bay lea', 'black pepper', 'bouillon', 'butter', 'cayenne pepper', 'chile powder', 'chili powder', 'chives', 'cilantro', 'cloves', 'cumin', 'curry powder', 'fennel', 'flour', 'garlic', 'ginger', 'herb', 'honey', 'hot sauce', 'ketchup', 'margarine', 'marjoram', 'mayonnaise', 'mustard', 'nutmeg', 'oil', 'onion', 'oregano', 'oyster sauce', 'paprika', 'parsley', 'pepper flakes', 'peppercorn', 'rosemary', 'sage', 'salt', 'seasoning', 'seed', 'soy sauce', 'spice', 'stock', 'sugar', 'thyme', 'vinegar', 'water', 'white pepper', 'worcestershire sauce']

GLUTEN_FREE = ['Hydrolyzed wheat protein', 'atta (chapati flour)', 'barley', 'beer', 'bulgur', 'cereal', 'crackers', 'durum', 'einkorn', 'emmer (type of wheat)', 'farina', 'faro', 'farro', 'fu', 'graham flour', 'gravy', 'kamut', 'malt', 'malt extract', 'malt flavoring', 'malt syrup', 'malt vinegar', 'malted milk', 'matzo', 'matzo meal', 'modified wheat starch', 'oat bran', 'oat flour', 'oatmeal', 'rye bread', 'rye flour', 'seitan', 'semolina', 'spelt', 'triticale', 'wheat bran', 'wheat flour', 'wheat germ', 'wheat starch', 'whole oats', 'yeast']

LACTOSE_FREE = ['butter', 'buttermilk', 'cheese', 'chocolate', 'cream', 'eggnog', 'ghee', 'ice-cream', 'kefir', 'milk', 'paneer', 'sour cream yakult', 'whey protein', 'yogurt']

NUT_FREE = ['almond', 'brazil nut', 'cashew nut', 'chestnut', 'hazelnut', 'macadamia', 'peanut', 'pecan', 'pili nut', 'pine nut', 'pistachio', 'tiger nut', 'walnut']

VEGAN = ['alligator', 'bacon', 'beef', 'buffalo', 'butter', 'cat', 'cheese', 'chicken', 'clam', 'crab', 'deer', 'dog', 'duck', 'egg', 'elephant', 'fish', 'frog', 'goat', 'gorilla', 'ham', 'honey', 'horse', 'kangaroo', 'lamb', 'lizard', 'mayonnaise', 'milk', 'monkey', 'moose', 'mouse', 'mussel', 'mutton', 'penguin', 'pigeon', 'pork', 'quail', 'rabbit', 'rat', 'salmon', 'shark', 'shellfish', 'snake', 'squirrel', 'tuna', 'turtle', 'urchin', 'veal', 'whale', 'yogurt']

VEGGIE = ['alligator', 'bacon', 'beef', 'buffalo', 'cat', 'chicken', 'clam', 'crab', 'deer', 'dog', 'duck', 'elephant', 'fish', 'frog', 'goat', 'gorilla', 'ham', 'horse', 'kangaroo', 'lamb', 'lizard', 'monkey', 'moose', 'mouse', 'mussel', 'mutton', 'penguin', 'pigeon', 'pork', 'quail', 'rabbit', 'rat', 'salmon', 'shark', 'shellfish', 'snake', 'squirrel', 'tuna', 'turtle', 'urchin', 'veal', 'whale']


# FIXME: delete below when satisfied with ingredients?

# import csv

# def get_diet_ingredients() -> list[str]:
#     thing = []
#     with open('./data/categories.csv') as fp:
#         csv_data = csv.reader(fp, skipinitialspace=True)
#         # heading = next(csv_data)
#         for row in csv_data:
#             if len(row) != 0:
#                 thing.append(row)
#     return thing
# for item in get_diet_ingredients():
#     print(item)

# def get_basic_ingreds() -> list[str]:
#     """
#     Reads basic ingredients from csv file,
#     returns sorted list of ingredients as lowercase string.
#     """

#     with open('./data/basic_ingredients.csv') as fp:
#         data = fp.readlines()
#     data = [line.lower().strip() for line in data]
#     data.sort()
#     return data

# BASIC_INGRED = get_basic_ingreds()

