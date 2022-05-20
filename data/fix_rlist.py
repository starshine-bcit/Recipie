import json
from pathlib import Path
import string


def main():
    dbpath = Path('.')
    datastores = list(dbpath.glob('*.json'))
    if len(datastores) < 1:
        raise ValueError('Error: no JSON datastores found')
    count = 0
    rdict = {}
    for file in datastores:
        with file.open('r', encoding='utf-8') as fileobject:
            data = json.load(fileobject)
            for x in data.values():
                try:
                    if type(x['title']) != str or type(x['ingredients']) != list or type(x['instructions']) != str or len(x['ingredients']) < 1:
                        continue
                    title = x['title']
                    title.translate(str.maketrans('', '', string.punctuation))
                    ingreds = [i for i in x['ingredients'] if i != '\n']
                    rdict.update({count: {
                        'title': title, 'ingreds': ingreds, 'instruct': x['instructions'], 'cat': []}})
                    count += 1
                except:
                    continue
        print(len(rdict))
    if len(rdict) > 0:
        outfile = Path('cleaned_recipes.json')
        with outfile.open('w', encoding='utf-8') as fobject:
            json.dump(rdict, fobject, indent=4)


if __name__ == '__main__':
    main()
