'''Module with constants for reference elsewhere'''

BASIC_INGREDS = ['baking', 'barbeque sauce', 'basil', 'bay lea', 'black pepper', 'bouillon', 'butter', 'cayenne pepper', 'chile powder', 'chili powder', 'chives', 'cilantro', 'cloves', 'cumin', 'curry powder', 'fennel', 'flour', 'garlic', 'ginger', 'herb', 'honey', 'hot sauce', 'ketchup', 'margarine', 'marjoram', 'mayonnaise', 'mustard', 'nutmeg', 'oil', 'onion', 'oregano', 'oyster sauce', 'paprika', 'parsley', 'pepper flakes', 'peppercorn', 'rosemary', 'sage', 'salt', 'seasoning', 'seed', 'soy sauce', 'spice', 'stock', 'sugar', 'thyme', 'vinegar', 'water', 'white pepper', 'worcestershire sauce']

GLUTEN_FREE = ['barley', 'yeast', 'bulgur', 'durum', 'farro', 'faro', 'graham flour', 'Hydrolyzed wheat protein', 'kamut', 'malt', 'malt extract', 'malt syrup', 'malt flavoring', 'malt vinegar', 'malted milk', 'matzo', 'matzo meal', 'modified wheat starch', 'oatmeal', 'oat bran', 'oat flour', 'whole oats', 'rye bread', 'rye flour', 'seitan', 'semolina', 'spelt', 'triticale', 'wheat bran', 'wheat flour', 'wheat germ', 'wheat starch', 'atta', 'chapati flour', 'einkorn', 'emmer', 'farina', 'fu', 'cereal', 'crackers', 'beer', 'gravy', 'wheat berries', 'wheat bran', 'wheat germ', 'pumpernickel', 'oat groats', 'couscous']

LACTOSE_FREE = ['blue cheese', 'comté', 'sharp provolone', 'red leicester', 'cottage cheese', 'american farmhouse cheddarsharp cheddar', 'mozzarella', 'gouda', 'cheddar', 'parmigiano-reggiano', 'pepper jack', 'monterey jack', 'pecorino romano', 'english farmhouse cheddar', 'cream cheese', 'swiss', 'parmigiano', 'provolone', 'brie', 'ricotta', 'feta', 'Colby-Jack', 'Muenster cheese', 'Gruyère cheese', 'buffalo mozzarella', 'camembert', 'irish cheddar', 'goat cheese', 'manchego', 'mascarpone', 'havarti', 'emmentalermilk', 'cheese', 'ice-cream', 'yogurt', 'butter', 'kefir', 'whey protein', 'cream', 'buttermilk', 'chocolate', 'eggnog', 'ghee', 'sour', 'cream', 'yakult', 'paneer']

NUT_FREE = ['almond', 'brazil nut', 'cashew nut', 'hazelnut', 'macadamia', 'pecan', 'pine nut', 'pistachio', 'walnut', 'chestnut', 'pili nut', 'tiger nut', 'peanut']

VEGAN = ['blue cheese', 'comté', 'sharp provolone', 'red leicester', 'cottage cheese', 'american farmhouse cheddarsharp cheddar', 'mozzarella', 'gouda', 'cheddar', 'parmigiano-reggiano', 'pepper jack', 'monterey jack', 'pecorino romano', 'english farmhouse cheddar', 'cream cheese', 'swiss', 'parmigiano', 'provolone', 'brie', 'ricotta', 'feta', 'Colby-Jack', 'Muenster cheese', 'Gruyère cheese', 'buffalo mozzarella', 'camembert', 'irish cheddar', 'goat cheese', 'manchego', 'mascarpone', 'havarti', 'emmentaler', 'milk', 'butter', 'yogurt', 'mayonnaise', 'honey', 'egg', 'beef', 'chicken', 'pork', 'lamb', 'mutton', 'fish', 'bacon', 'moose', 'kangaroo', 'alligator', 'veal', 'buffalo', 'snake', 'goat', 'deer', 'horse', 'rabbit', 'squirrel', 'pigeon', 'quail', 'turtle', 'duck', 'ham', 'shellfish', 'clam', 'crab', 'mussel', 'salmon', 'tuna', 'urchin', 'penguin', 'shark', 'whale', 'dog', 'cat', 'frog', 'lizard', 'elephant', 'monkey', 'gorilla', 'mouse', 'rat']

VEGGIE = ['beef', 'chicken', 'pork', 'lamb', 'mutton', 'fish', 'bacon', 'moose', 'kangaroo', 'alligator', 'veal', 'buffalo', 'snake', 'goat', 'deer', 'horse', 'rabbit', 'squirrel', 'pigeon', 'quail', 'turtle', 'duck', 'ham', 'shellfish', 'clam', 'crab', 'mussel', 'salmon', 'tuna', 'urchin', 'penguin', 'shark', 'whale', 'dog', 'cat', 'frog', 'lizard', 'elephant', 'monkey', 'gorilla', 'mouse', 'rat']


# FIXME: delete below when satisfied with ingredients?

# import csv

# def get_diet_ingredients() -> list[str]:
#     thing = []
#     with open('./data/categories.csv', encoding='UTF-8') as fp:
#         csv_data = csv.reader(fp, skipinitialspace=True)
#         # heading = next(csv_data)
#         for row in csv_data:
#             if len(row) != 0:
#                 thing.append(row)
#     return thing
# for item in get_diet_ingredients():
#     item = [i.strip() for i in item]
#     print()
#     print(item)
# print()


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

