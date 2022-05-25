# ACIT2911 Project - Recipie

Git repository for group 19's ACIT2911 project, Recipie

## Recipie Details

A Python based application that users can look up cooking recipes for.
Features include:
- A button that randomly generates a recipe
- An input field for ingredients that the user has, returns a list of recipes that include only those ingredients or less
- A category list for users with dietary restrictions, filters out recipes that do not meet the category


## Members

Amanda
Eva
Raqin
Sasha
Sean


## Usage 

```text
Usage: recipie.py [-h] [-v] [-ds DATASTORE]

Recipie desktop application 

Options: 
-h, --help                              show this help message and exit 
-v, --verbose                           verbosely output to console 
-ds DATASTORE, --datastore DATASTORE    json file with recipes load 
```

Steps to run Recipie Application: 
1. Open the git console, `mkdir [FOLDER_NAME]` to create a folder and `cd [FOLDER_NAME]` change to the directory. 
2. `git clone https://github.com/SeanXYTan/ACIT2911.git` to copy Recipie repository into your local directory. 
3. `cd ACIT2911` to change directory to ACIT2911. 
4. To run Recipie from source, you need to install `PyQt6` PyPi Package by typing `pip install pyqt6` in the console. 
5. To open the Recipie program, `py .\recipie.py` for Windows and `python3 ./recipie.py` for Linux.


## Standalone Installation 

1. Locate "Release" and click "tags"
2. Select the latest version of release 
3. Download the Windows installer by selecting the asset ending in .exe
4. From "Download," click "open file" to complete the installation 


## Adding New Recipes 

User can choose to add a new recipe to the last existing JSON or create a new JSON.\
All recipes are inserted using JSON format, and each recipe as a value is assigned a numerical key.\
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


## Acknowledgements

This project uses open source tools and libraries from the Qt project to generate a GUI, in accordance with the GPLv3 License.

* [Qt.io](https://www.qt.io/product/features?hsLang=en#js-6-4)
* [Recipe Json](https://eightportions.com/datasets/Recipes/)
