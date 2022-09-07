# ACIT2911 Project - Recipie

A project created for ACIT 2911 (Winter Term 2022) by team Voracious Hippos.


## Recipie Details

Recipie is a Python-based application for users to look up cooking recipes.
Features include:
- Displaying a random recipe
- Searching for recipes by desired ingredients
- Filtering recipes based on dietary restrictions
- Saving recipes as favourites
- Printing recipes
- Application runs completely offline
- Ability to add additional recipes via json data-stores


## Voracious Hippos Team Members

- Amanda
- Eva
- Raqin
- Sasha
- Sean

## Requirements

### Software
* python >= 3.9
* PyQt6 >= 6.30\
Binary Windows releases can be run without these

### Operating System
* Windows NT based system
   * Tested on Win 10/11
* GNU/Linux with X11 and a modern DE
   * Tested on Debian 11 with XFCE
* MacOS
   * Not tested, but should work

### Hardware
* 1024x768+ display
* 500 MB of available memory
* 64-bit processor

## Usage 

```text
Usage: recipie.py [-h] [-v] [-ds DATASTORE]

Recipie desktop application 

Options: 
-h, --help                              show this help message and exit 
-v, --verbose                           verbosely output to console 
-ds DATASTORE, --datastore DATASTORE    folder with json recipes to load (default: ./data)
```

Steps to run Recipie Application: 

1. `git clone https://github.com/starshine-bcit/Recipie.git` to copy the Recipie repository into a local directory. 
2. `cd Recipie` to change directory to Recipie. 
3. To run Recipie from source, you need to install `PyQt6` PyPi Package by typing `pip install pyqt6` in the console. 
4. To open the Recipie program, `py .\recipie.py` for Windows and `python3 ./recipie.py` for Linux.


## Standalone Installation 

1. On GitHub, locate "Releases", and click "tags" 
2. Select the latest version of release 
3. Download the Windows installer by selecting the asset ending in .exe 
4. From "Downloads", click "open file" to complete the installation 


## Adding New Recipes 

User can choose to add a new recipe to the last existing JSON or create a new JSON.\
All recipes are inserted using JSON format.\
Each recipe is a value that is assigned to a numerical key. Each key must be unique.\
The recipe "value" is another dictionary with the following keys: 

1. title            
    * value: string
2. ingreds          
    * value: list of string(s) items
3. instruct         
    * value: string
4. cat              
    * value: list of string(s) items 
    * category must be 'glutenfree', 'lactosefree', 'nutfree', 'vegetarian', 'vegan' 

Once you're done with the JSON file, you can move the JSON into the ./data folder, located inside the repo you cloned. (e.g. `ACIT2911/data/your file here`)
Alternatively, you can use the `-ds` option when initializing the app to designate where your recipe json is located.

## Acknowledgements

This project uses open source tools and libraries from the Qt project to generate a GUI, in accordance with the GPLv3 License. This project is also licensed GPLv3, which can be viewed in the LICENSE file.

* [Qt.io](https://www.qt.io/product/features?hsLang=en#js-6-4)
* [Recipe Json](https://eightportions.com/datasets/Recipes/)
