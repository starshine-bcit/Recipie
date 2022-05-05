'''Recipie module for subclassing and event handling'''
import sys
from random import choice
#import argparse
#from pathlib import Path

from PyQt6 import QtCore, QtGui, QtWidgets

from qtui import Ui_MainWindow


class MainWindowRecipie(Ui_MainWindow):
    def __init__(self, verbose, rlist) -> None:
        super().__init__()
        self.rlist = rlist
        self.verbose = verbose

    def createevents(self):
        '''Connect triggered events with functions'''
        self.pushButtonRandom.clicked.connect(self.random_button_click)
        self.actionRandom.triggered.connect(self.random_button_click)
        self.actionExit.triggered.connect(self.exit_recipie)

    def linkimages(self, app):
        '''Link image files to window'''
        self.labelRecipieLogo.setPixmap(
            QtGui.QPixmap('./image/RecipieLogo.png'))
        app_icon = QtGui.QIcon()
        app_icon.addFile('./image/RecipieLogo_icon.png', QtCore.QSize(16, 16))
        app_icon.addFile('./image/RecipieLogo_icon.png', QtCore.QSize(24, 24))
        app_icon.addFile('./image/RecipieLogo_icon.png', QtCore.QSize(32, 32))
        app_icon.addFile('./image/RecipieLogo_icon.png', QtCore.QSize(48, 48))
        app_icon.addFile('./image/RecipieLogo_icon.png',
                         QtCore.QSize(256, 256))
        app.setWindowIcon(app_icon)

    def random_button_click(self):
        '''Call rrecipe, then display it with display_recipe'''
        rrecipe = return_rrecipe(self.rlist)
        if self.verbose:
            print(
                f'Random event captured\n'
                f'Selecting random recipe {rrecipe.name} and displaying...'
            )
        self.display_recipe(
            rrecipe.name, rrecipe.ingredients, rrecipe.instructions)

    def display_recipe(self, title, ingred, instruct):
        '''Display chosen recipe in the main window'''
        self.labelRecipeName.setText(title)
        self.textBrowserRecipeIngredients.setText(ingred)
        self.textBrowserRecipeDirections.setText(instruct)

    def exit_recipie(self):
        '''Exit the entire program'''
        if self.verbose:
            print('Exiting Recipie\n')
        sys.exit(0)


def return_rrecipe(rlist):
    '''Return a random recipe class instance from a list of them'''
    return choice(rlist.recipes)


# def parserecipe(rrecipe):
#     title = rrecipe.get('title')
#     ingred = rrecipe.get('ingredients')
#     ingred_parsed = ''
#     for x in ingred:
#         ingred_parsed += x + '\n'
#     instruct = rrecipe.get('instructions')
#     return title, ingred_parsed, instruct


def initmainwindow(verbose, rlist):
    if verbose:
        print('Starting to initialize ui...')
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowRecipie(verbose, rlist)  # Instance of UI_MainWindow
    ui.setupUi(MainWindow)  # Basic initialization
    ui.createevents()  # Adding event listeners
    ui.linkimages(app)  # Link images to window
    MainWindow.show()
    if verbose:
        print('Initialized successfully and visible')
    sys.exit(app.exec())


if __name__ == '__main__':
    pass
    # parser = argparse.ArgumentParser(description='Recipie desktop application')

    # parser.add_argument(
    #     '-v',
    #     '--verbose',
    #     action = 'store_true',
    #     help = 'verbosely output to console'
    # )

    # parser.add_argument(
    #     '-ds',
    #     '--datastore',
    #     type = Path,
    #     default = Path('./data'),
    #     help = 'json file to load, hopefully with recipies'
    # )

    # args = parser.parse_args()
    # if verbose: print(
    #     f'Parsed command line arguments:'
    #     f'\n{args}\n'
    # )
    # rlist = []
    # initmainwindow(args, rlist)
