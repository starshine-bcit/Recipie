'''Module with constants for reference elsewhere'''

BASIC_INGREDS = ['baking', 'barbeque sauce', 'basil', 'bay lea', 'black pepper', 'bouillon', 'butter', 'cayenne pepper', 'chile powder', 'chili powder', 'chives', 'cilantro', 'cloves', 'cumin', 'curry powder', 'fennel', 'flour', 'garlic', 'ginger', 'herb', 'honey', 'hot sauce', 'ketchup', 'margarine', 'marjoram', 'mayonnaise', 'mustard', 'nutmeg', 'oil', 'onion', 'oregano', 'oyster sauce', 'paprika', 'parsley', 'pepper flakes', 'peppercorn', 'rosemary', 'sage', 'salt', 'seasoning', 'seed', 'soy sauce', 'spice', 'stock', 'sugar', 'thyme', 'vinegar', 'water', 'white pepper', 'worcestershire sauce']

GLUTEN_FREE = ['atta', 'bagel', 'barley', 'beer', 'bread', 'bulgur', 'cereal', 'chapati flour', 'couscous', 'cracker', 'crouton', 'durum', 'einkorn', 'emmer', 'farina', 'faro', 'farro', 'fu', 'graham flour', 'granola', 'gravy', 'kamut', 'malt', 'matzo', 'noodle', 'oat', 'oat groats', 'orzo', 'pasta', 'pumpernickel', 'purpose flour', 'rye', 'rye', 'seitan', 'semolina', 'soy sauce', 'spelt', 'triticale', 'udon', 'wheat', 'yeast']

LACTOSE_FREE = ['asiago', 'blue cheese', 'brie', 'butter', 'buttermilk', 'camembert', 'cheddar', 'cheese', 'chocolate', 'colby-jack', 'comte', 'comté', 'cottage cheese', 'cream', 'cream cheese', 'edam', 'eggnog', 'emmental', 'feta', 'ghee', 'goat cheese', 'gorgonzola', 'gouda', 'gruyere', 'gruyère', 'halloumi', 'havarti', 'ice-cream', 'kefir', 'manchego', 'mascarpone', 'milk', 'monterey jack', 'mozzarella', 'muenster cheese', 'paneer', 'parmesan', 'parmigiano', 'pecorino romano', 'pepper jack', 'provolone', 'quark', 'queso', 'raclette', 'red leicester', 'ricotta', 'roquefort', 'swiss', 'whey protein', 'yakult', 'yoghurt', 'yogurt']

NUT_FREE = ['almond', 'arachis', 'brazil nut', 'cashew nut', 'chestnut', 'filbert', 'hazelnut', 'hickory nut', 'macadamia', 'mandelona', 'marzipan', 'peanut', 'pecan', 'pili nut', 'pine nut', 'pistachio', 'tiger nut', 'walnut']

VEGGIE = ['alligator', 'anchov', 'bacon', 'basa', 'bass', 'beaver', 'beef', 'buffalo', 'calamari', 'carp', 'cat', 'char', 'chicken', 'clam', 'cockroach', 'cod', 'crab', 'deer', 'dog', 'duck', ' eel', 'elephant', 'escargot', 'fish', 'flounder', 'frog', 'goat', 'gorilla', 'grouper', 'haddock', 'hailbut', 'ham', 'herring', 'horse', 'kangaroo', 'lamb', 'lizard', 'lobster', 'mackerel', 'mahi mahi', 'mahi-mahi', 'monkey', 'moose', 'mouse', 'mussel', 'mutton', 'octopus', 'ostrich', 'oyster', 'penguin', 'perch', 'pig', 'pigeon', 'pike', 'pollock', 'pork', 'pot roast', 'quail', 'rabbit', 'rat', 'ribs', 'roughy', 'salmon', 'sardine', 'sausage', 'scallop', 'shad', 'shark', 'shellfish', 'shrimp', 'snail', 'snake', 'snapper', 'squid', 'squirrel', 'steak', 'tilapia', 'trout', 'tuna', 'turtle', 'urchin', 'veal', 'venison', 'whale', 'yellowtail']

VEGAN = LACTOSE_FREE + VEGGIE + ['egg', 'gelatin', 'honey', 'isinglass', 'lard', 'mayonnaise', 'shellac', 'tallow']
VEGAN.sort()

# FIXME: delete below when satisfied with ingredients?

# import csv

# def get_diet_ingredients() -> list[str]:
#     thing = []
#     with open('./data/categories.csv', encoding='UTF-8') as fp:
#         # csv_data = csv.reader(fp, skipinitialspace=True)
#         csv_data = csv.reader(fp)
#         # heading = next(csv_data)
#         for row in csv_data:
#             if len(row) != 0:
#                 thing.append(row)
#     return thing
# for item in get_diet_ingredients():
#     # item = [i.strip() for i in item]
#     item = [i for i in item]
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

# if __name__ == "__main__":
#     print(VEGAN)