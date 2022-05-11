'''Recipie module for subclassing and event handling'''
import sys
import re

from PyQt6 import QtCore, QtGui, QtWidgets, QtPrintSupport

from .qtui import Ui_MainWindow
from .recipelist import RecipeList
from .recipe import Recipe


class MainWindowRecipie(Ui_MainWindow):
    """Main Window of Recipie, sub-classed from qtui.Ui_MainWindow
        Contains a variety of functions and methods to manipulate UI

    Args:
        Ui_MainWindow (Ui_MainWindow): Ui_MainWindow class to subclass off of

    Attributes:
        rlist (RecipeList): Main working RecipeList instance
        verbose (bool): Enables logging useful messages to console
    """

    def __init__(self, verbose: bool, rlist: RecipeList) -> None:
        """Initialize this instance with provided args
        Use super().__init__() just in case

        Args:
            verbose (bool): True enables logging to console
            rlist (RecipeList): Instance of RecipeList with all recipes
        """

        super().__init__()
        self.rlist = rlist
        self.srlist = {}
        self.verbose = verbose

    def setupUicustom(self):
        self.printer = QtPrintSupport.QPrinter()
        self.curr_recipe_md = QtGui.QTextDocument()
        self.labelStatusBarRecipeCount = QtWidgets.QLabel(
            f'Indexing {len(self.rlist.recipes)} recipes ')
        self.statusbar.addPermanentWidget(self.labelStatusBarRecipeCount)
        self.statusbar.showMessage('Ready')
        self.tabWidgetRecipe.setCurrentIndex(0)
        self.tabWidgetSearch.setCurrentIndex(0)

    def createevents(self) -> None:
        '''Connect triggered events with functions'''

        self.pushButtonRandom.clicked.connect(self.random_button_click)
        self.actionRandom.triggered.connect(self.random_button_click)
        self.actionExit.triggered.connect(self.exit_recipie)
        self.actionRemove_Selected.triggered.connect(
            self.remove_selected_search)
        self.actionReset_Search.triggered.connect(self.reset_search)
        self.commandLinkButtonEnterIngredient.clicked.connect(
            self.enter_search_term)
        self.radioButtonExclusive.clicked.connect(self.call_search)
        self.radioButtonInclusive.clicked.connect(self.call_search)
        self.pushButtonRemoveSelected.clicked.connect(
            self.remove_selected_search)
        self.pushButtonResetSearch.clicked.connect(self.reset_search)
        self.pushButtonRecipeClear.clicked.connect(self.clear_recipe_display)
        self.actionPrint.triggered.connect(self.call_print)
        self.listWidgetSearchResults.itemDoubleClicked.connect(
            self.click_search_result)

        self.actionExit.setShortcut(QtGui.QKeySequence('Ctrl+Q'))
        self.actionPrint.setShortcut(QtGui.QKeySequence('Ctrl+P'))
        self.actionRandom.setShortcut(QtGui.QKeySequence('Ctrl+R'))
        QtGui.QShortcut(QtGui.QKeySequence.StandardKey.InsertParagraphSeparator,
                        self.lineEditIngredientEntry, activated=self.enter_search_term)

    def linkimages(self, app: QtWidgets.QApplication) -> None:
        '''Link image files to application

        Args:
            app (QtWidgets.Qapplication):
                An instance of a QApplication to link images to
        '''
        # Set our main logo image
        self.labelRecipieLogo.setPixmap(
            QtGui.QPixmap('./image/NewRecipieLogo.png'))

        # Setup our QIcon instance for the window icon
        app_icon = QtGui.QIcon()
        app_icon.addFile('./image/PieLogo64.png', QtCore.QSize(16, 16))
        app_icon.addFile('./image/PieLogo64.png', QtCore.QSize(24, 24))
        app_icon.addFile('./image/PieLogo64.png', QtCore.QSize(32, 32))
        app_icon.addFile('./image/PieLogo64.png', QtCore.QSize(48, 48))
        app_icon.addFile('./image/PieLogo256.png',
                         QtCore.QSize(256, 256))

        # Finally, set app icon to the QIcon instance
        app.setWindowIcon(app_icon)

    def random_button_click(self) -> None:
        '''Call get_random_recipe, display it with display_recipe'''

        rrecipe = self.rlist.get_random_recipe()
        if self.verbose:
            print(
                f'Random event captured\n'
                f'Selecting random recipe {rrecipe.name} and displaying...'
            )

        self.display_recipe(rrecipe)

    def display_recipe(self, rcp: Recipe) -> None:
        '''Display chosen recipe in the main window'''

        ingreds = rcp.ingredients_as_str()

        self.labelRecipeName.setText(rcp.name)
        self.textBrowserRecipeIngredients.setText(ingreds)
        self.textBrowserRecipeDirections.setText(rcp.instructions)
        self.set_md_recipe(rcp.name, ingreds, rcp.instructions)

    def exit_recipie(self) -> None:
        '''Exit the entire program'''

        if self.verbose:
            print('Exiting Recipie\n')
        sys.exit(0)

    def status_bar_display(self, message: str) -> None:
        '''
        Set status bar display message
            Also initializes recipe count widget if not done already

            Args:
                message (str):
                    Message to display on left side of status bar 
        '''

        self.statusbar.showMessage(message)

    def enter_search_term(self) -> None:
        '''Captures text from user entry and inputs to search list'''

        stext = self.lineEditIngredientEntry.text()
        self.lineEditIngredientEntry.setText('')
        newitem = QtWidgets.QListWidgetItem(stext)
        self.listWidgetSearchInput.addItem(newitem)
        self.call_search()

    def call_search(self) -> None:
        '''Sends list of user search terms to logic search functions'''

        self.listWidgetSearchResults.clear()
        search_terms = [self.listWidgetSearchInput.item(
            x).text() for x in range(self.listWidgetSearchInput.count())]
        if self.verbose:
            print(
                f'Sending these terms to search:\n{search_terms}'
            )
        if len(search_terms) > 0:
            if self.radioButtonExclusive.isChecked():
                # self.srlist = function call
                pass
            elif self.radioButtonInclusive.isChecked():
                # self.srlist = function call
                pass
            self.display_search_result_list()
        else:
            self.srlist.clear()
            if self.verbose:
                print('Search called, but no items to search for')

    def reset_search(self) -> None:
        '''Clear Search inputs and results'''

        self.listWidgetSearchInput.clear()
        self.listWidgetSearchResults.clear()
        self.tabWidgetRecipe.setCurrentIndex(0)
        self.tabWidgetSearch.setCurrentIndex(0)
        self.radioButtonInclusive.setChecked(True)
        self.srlist.clear()
        self.status_bar_display('Ready')
        if self.verbose:
            print('Resetting search...')

    def remove_selected_search(self) -> None:
        '''Remove user selected items from search input'''

        for listitem in self.listWidgetSearchInput.selectedItems():
            self.listWidgetSearchInput.takeItem(
                self.listWidgetSearchInput.row(listitem))
        if self.verbose:
            print('Removing selected items...')
        self.call_search()

    def clear_recipe_display(self) -> None:
        '''Clear currently displayed recipe, for reasons'''

        self.labelRecipeName.setText('Recipe Name')
        self.textBrowserRecipeIngredients.setText('')
        self.textBrowserRecipeDirections.setText('')
        self.curr_recipe_md.setMarkdown('')
        if self.verbose:
            print('Clearing displayed recipe...')

    def call_print(self) -> None:
        '''Open print dialogue for current selected recipe'''

        self.print_dialog = QtPrintSupport.QPrintDialog(self.printer)
        self.print_dialog.open(self.send_print)

    def send_print(self) -> None:
        '''Send document to configured printer'''

        self.curr_recipe_md.print(self.printer)

    def set_md_recipe(self, title: str, ingred: str, instruct: str):
        '''_summary_

        Args:
            title (str): title of recipe
            ingred (str): ingredients of recipe
            instruct (str): instructions of recipe
        '''

        ingred = ingred.replace('\n', '\n- ')
        ingred = '- ' + ingred
        finstruct = ''
        count = 0
        instructnums = re.split(r'\d{0,2}\.[: \n\t:]', instruct)
        instructper = instruct.split('. ')

        if len(instructnums) > len(instructper):
            instructper = instructnums
        for x in instructper:
            count += 1
            temp = str(count) + '. ' + x + '\n'
            finstruct += temp

        self.curr_recipe_md.setMarkdown(
            f'# {title}\n'
            f'## Ingredients\n'
            f'{ingred}\n'
            f'## Instructions:\n'
            f'{finstruct}'
        )

    def display_search_result_list(self) -> None:
        '''Displays list of recipes in search bar'''

        for x in range(10):
            self.srlist.update({x: self.rlist.recipes[x]})
        srlistlen = len(self.srlist)

        for x in range(srlistlen):
            newname = self.srlist[x].name
            newitem = QtWidgets.QListWidgetItem(newname)
            self.listWidgetSearchResults.addItem(newitem)

        self.status_bar_display(f'Found {srlistlen} results')
        self.tabWidgetRecipe.setCurrentIndex(1)

    def click_search_result(self) -> None:
        '''Display search result when clicked on'''

        currindex = self.listWidgetSearchResults.currentRow()
        self.display_recipe(self.srlist[currindex])
        self.tabWidgetRecipe.setCurrentIndex(0)
        if self.verbose: print(f'Display recipe at index {currindex}')

def initmainwindow(verbose: bool, rlist: RecipeList) -> None:
    '''Initialize and display main recipie window

        Args:
            verbose (bool): Specify verbose setting for program
            rlist (RecipeList): Main instance of RecipeList
    '''

    if verbose:
        print('Starting to initialize ui...')
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowRecipie(verbose, rlist)  # Instance of UI_MainWindow
    ui.setupUi(MainWindow)  # Basic initialization
    ui.setupUicustom()  # Our secondary initialization
    ui.createevents()  # Add event listeners and shortcuts
    ui.linkimages(app)  # Link images to window
    ui.status_bar_display('Ready')
    MainWindow.show()  # Finally, show the window
    if verbose:
        print('Initialized successfully and visible')
    sys.exit(app.exec())


if __name__ == '__main__':
    pass
