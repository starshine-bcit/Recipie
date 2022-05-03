'''Recipie module for subclassing and event handling'''
import sys
from PyQt6 import QtCore, QtGui, QtWidgets

# To make an environment to reach other folder
# $ENV:PYTHONPATH = "C:\Courses\ACIT-2911\project\ACIT2911"

from testing.qtuitest import Ui_MainWindow
from testing.rstore import return_rrecipe
# Subclass things here for events from mainwindow?


class MainWindowTest(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()

    def updateui(self):
        self.pushButtonRandom.clicked.connect(self.random_button_click)

    def random_button_click(self):
        title, ingred, instruct = parserecipe(return_rrecipe())
        # print(title)
        # print(ingred)
        # print(instruct)
        self.display_recipe(title, ingred, instruct)

    def display_recipe(self, title, ingred, instruct):
        self.labelRecipeName.setText(title)
        self.textBrowserRecipeIngredients.setText(ingred)
        self.textBrowserRecipeDirections.setText(instruct)


def parserecipe(rrecipe):
    title = rrecipe.get('title')
    ingred = rrecipe.get('ingredients')
    ingred_parsed = ''
    for x in ingred:
        ingred_parsed += x + '\n'
    instruct = rrecipe.get('instructions')
    return title, ingred_parsed, instruct


def main():
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowTest()
    ui.setupUi(MainWindow)
    ui.updateui()
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
