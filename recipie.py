'''Recipie Main Module'''
import sys
from pathlib import Path
import argparse

from modules.revent import initmainwindow
from modules.recipelist import RecipeList


def createdslist(args):
    '''Create a list of files from the supplied directory'''
    datafilelist = list(args.datastore.glob('*.json'))
    if len(datafilelist) < 1:
        raise ValueError('Error: no JSON datastores found')
    return datafilelist


def main():
    '''Main recipie function to initiate/load everything else'''
    parser = argparse.ArgumentParser(description='Recipie desktop application')

    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='verbosely output to console'
    )

    parser.add_argument(
        '-ds',
        '--datastore',
        type=Path,
        default=Path(__file__).parent.joinpath('data'),
        help='json file to load, hopefully with recipies'
    )

    args = parser.parse_args()
    if args.verbose:
        print(
            f'Parsed command line arguments:'
            f'\n{args}\n'
        )

    verbose = True if args.verbose else False
    datafilelist = createdslist(args)
    mainrlist = RecipeList(datafilelist)
    if verbose:
        print(f'Total recipes indexed: {len(mainrlist.recipes)}')
    initmainwindow(verbose, mainrlist)



if __name__ == '__main__':
    main()
