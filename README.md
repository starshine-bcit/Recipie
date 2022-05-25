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
1. Open the git console, create a folder (`mkdir [FOLDER_NAME]`) and change to the directory (`cd [FOLDER_NAME]`). 
2. `git clone https://github.com/SeanXYTan/ACIT2911.git` to copy Recipie repository into your local directory. 
3. `cd ACIT2911` to change directory to ACIT2911. 
4. `code .` to open the source. 
5. To run Recipie from source, you need to install `PyQt6` PyPi Package by typing `pip install pyqt6` in the console. 
6. `py ./recipie.py` to open up Recipie program 


## Standalone Installation 

1. Locate "Release" and click "tags"
2. Select the latest version of release 
3. Download Windows installer by selecting the asset ends with .exe
4. From "Download," click "open file" to complete installation 


## Acknowledgements

This project uses open source tools and libraries from the Qt project to generate a GUI, in accordance with the GPLv3 License.

* [Qt.io](https://www.qt.io/product/features?hsLang=en#js-6-4)
* [Recipe Json](https://eightportions.com/datasets/Recipes/)
