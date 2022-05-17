import json
from pathlib import Path
import string


json1 = Path('recipes_ar_clean.json')
json2 = Path('recipes_raw_epi.json')
json3 = Path('recipes_raw_fn.json')
jsonfiles = [json1, json2, json3]
rdict = {}
count = 0

for file in jsonfiles:
    with file.open('r', encoding='utf-8') as fobject:
        dfile = json.load(fobject)

    for val in dfile.values():
        try:
            if len(val['title']) < 1 or len(val['ingredients']) < 1 or len(val['instructions']) < 1:
                continue
            title = val['title']
            title.translate(str.maketrans('', '', string.punctuation))
            ingreds = [i for i in val['ingredients'] if i != '\n']
            rdict.update({
                count: {
                    'title': title,
                    'ingred': ingreds,
                    'instruct': val['instruct'],
                    'cat': 'Null'
                }
            })
            count += 1
        except:
            continue
    print(len(rdict))
if len(rdict) > 100000:
    outfile = Path('cleaned_recipes')
    with outfile.open('r', encoding='utf-8') as fobject:
        json.dump(rdict, outfile, indent = 4)