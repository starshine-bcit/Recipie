'''Recipie Main Module'''
# Import from ./modules here
from pathlib import Path
import argparse

from PyQt6 import QtCore, QtGui, QtWidgets

import modules.revent
import modules.qtui

def main():
    '''Main recipie function to initiate/load everything else'''
    parser = argparse.ArgumentParser(description='Recipie desktop application')

    parser.add_argument(
        '-v',
        '--verbose',
        action = 'store_true',
        help = 'verbosely output to console'
    )

    parser.add_argument(
        '-ds',
        '--datastore',
        type = Path,
        default = Path('./data'),
        help = 'json file to load, hopefully with recipies'
    )

    args = parser.parse_args()
    if args.verbose: print(
        f'Parsed command line arguments:'
        f'\n{args}\n'
    )

    # Insert recipe class instantion routine
    # Return rlist here to pass to into initmainwindow()
    modules.revent.initmainwindow(args, rlist)


if __name__ == '__main__':
    main()
