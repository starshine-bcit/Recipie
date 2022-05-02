# Import from ./modules here
from pathlib import Path
import argparse

def main():
    #This section creates and parses arguments to the main program
    parser = argparse.ArgumentParser(description='Recipie desktop application')

    parser.add_argument(
        '-v',
        '--verbose',
        action = 'store_true',
        help = 'verbosely output to console'
    )

    #Change default to datastore locaion
    parser.add_argument(
        '-ds',
        '--datastore',
        type = Path,
        default = Path('./data.json'),
        help = 'json file to load, hopefully with recipies'
    )

    args = parser.parse_args()

    #Call event loop here

if __name__ == '__main__':
    main()