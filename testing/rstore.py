'''Test load and initialization of recipe JSON module'''
from pathlib import Path
import json
from collections import OrderedDict
from random import choice

def return_rrecipe():
    rpath = Path('./recipes_ar_clean.json')
    with rpath.open('r', encoding='utf-8') as rfile:
        tdata = OrderedDict()
        tdata = json.load(rfile)

    rrecipe = choice(list(tdata.values()))
    frecipe = list(tdata.items())[0]

    return rrecipe

def main():
    rpath = Path('./recipes_ar_clean.json')
    with rpath.open('r', encoding='utf-8') as rfile:
        tdata = OrderedDict()
        tdata = json.load(rfile)
    
    rrecipe = choice(list(tdata.values()))
    frecipe = list(tdata.items())[0]

    print(
        f'Total length of recipes:\n{len(tdata)}\n'
        f'\nFirst recipe in the dict:\n{frecipe}\n'
        f'\nRandom Recipe:\n{rrecipe}\n'
    )


if __name__ == '__main__':
    main()
