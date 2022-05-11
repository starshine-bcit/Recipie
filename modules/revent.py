'''Recipie module for subclassing and event handling'''
import sys
import re

from PyQt6 import QtCore, QtGui, QtWidgets, QtPrintSupport

from .qtui import Ui_MainWindow
from .recipelist import RecipeList


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
        self.verbose = verbose

    def createevents(self) -> None:
        '''Connect triggered events with functions'''

        self.pushButtonRandom.clicked.connect(self.random_button_click)
        self.actionRandom.triggered.connect(self.random_button_click)
        self.actionExit.triggered.connect(self.exit_recipie)
        self.actionRemove_Selected.triggered.connect(self.remove_selected_search)
        self.actionReset_Search.triggered.connect(self.reset_search)
        self.commandLinkButtonEnterIngredient.clicked.connect(
            self.enter_search_term)
        self.radioButtonExclusive.clicked.connect(self.call_search)
        self.radioButtonInclusive.clicked.connect(self.call_search)
        self.pushButtonRemoveSelected.clicked.connect(self.remove_selected_search)
        self.pushButtonResetSearch.clicked.connect(self.reset_search)
        self.pushButtonRecipeClear.clicked.connect(self.clear_recipe_display)
        self.actionPrint.triggered.connect(self.call_print)

    def init_keyboard_shortcuts(self) -> None:
        '''Create keyboard shortcuts based on event defined above'''
        
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

        # In this case, we pass the ingredients as a string
        ingreds = rrecipe.ingredients_as_str()
        #ingreds.replace('\n', '\n\u2022 ')
        self.display_recipe(
            rrecipe.name, ingreds, rrecipe.instructions)

    def display_recipe(self, title: str, ingred: str, instruct: str) -> None:
        '''Display chosen recipe in the main window'''

        self.labelRecipeName.setText(title)
        self.textBrowserRecipeIngredients.setText(ingred)
        self.textBrowserRecipeDirections.setText(instruct)
        self.update_qtext_print(title, ingred, instruct)

    def exit_recipie(self) -> None:
        '''Exit the entire program'''

        if self.verbose:
            print('Exiting Recipie\n')
        sys.exit(0)

    def status_bar_display(self, message: str) -> None:
        '''Set status bar display message
            Also initializes recipe count widget if not done already

            Args:
                message (str):
                    Message to display on left side of status bar 
        '''

        self.statusbar.showMessage(message)

        # Call init function if Qlabel doesn't exist
        try:
            if self.labelStatusBarRecipeCount:
                pass
        except AttributeError:
            self.init_status_recipe_count()

    def init_status_recipe_count(self) -> None:
        '''Initialize and display recipe count status bar widget'''

        self.labelStatusBarRecipeCount = QtWidgets.QLabel(
            f'Indexing {len(self.rlist.recipes)} recipes ')
        self.statusbar.addPermanentWidget(self.labelStatusBarRecipeCount)

    def enter_search_term(self) -> None:
        '''Captures text from user entry and inputs to search list'''

        stext = self.lineEditIngredientEntry.text()
        self.lineEditIngredientEntry.setText('')
        newitem = QtWidgets.QListWidgetItem(stext)
        self.listWidgetSearchInput.addItem(newitem)
        self.call_search()

    def call_search(self) -> None:
        '''Sends list of user search terms to logic search functions'''

        search_terms = [self.listWidgetSearchInput.item(x).text() for x in range(self.listWidgetSearchInput.count())]
        if self.verbose:
            print(
                f'Sending these terms to search:\n{search_terms}'
            )
        if len(search_terms) > 0:
            if self.radioButtonExclusive.isChecked():
                pass
            elif self.radioButtonInclusive.isChecked():
                pass
            # Pass search_terms to logic search functions here
        else:
            if self.verbose:
                print('Search called, but no items to search for')

    def reset_search(self) -> None:
        '''Clear Search inputs and results'''

        self.listWidgetSearchInput.clear()
        self.listWidgetSearchResults.clear()
        self.tabWidgetRecipe.setCurrentIndex(0)
        self.tabWidgetSearch.setCurrentIndex(0)
        self.radioButtonInclusive.setChecked(True)
        if self.verbose: print('Resetting search...')

    def remove_selected_search(self) -> None:
        '''Remove user selected items from search input'''

        for listitem in self.listWidgetSearchInput.selectedItems():
            self.listWidgetSearchInput.takeItem(self.listWidgetSearchInput.row(listitem))
        if self.verbose: print('Removing selected items...')
        self.call_search()

    def clear_recipe_display(self) -> None:
        '''Clear currently displayed recipe, for reasons'''

        self.labelRecipeName.setText('Recipe Name')
        self.textBrowserRecipeIngredients.setText('')
        self.textBrowserRecipeDirections.setText('')
        if self.verbose: print('Clearing displayed recipe...')

    def init_print(self) -> None:
        '''Initialize print functionality'''

        self.printer = QtPrintSupport.QPrinter()
        self.curr_recipe_text = QtGui.QTextDocument()

    def call_print(self) -> None:
        '''Open print dialogue for current selected recipe'''

        self.print_dialog = QtPrintSupport.QPrintDialog(self.printer)
        self.print_dialog.open(self.send_print)

    def send_print(self) -> None:
        '''Send document to configured printer'''

        self.curr_recipe_text.print(self.printer)
    
    def update_qtext_print(self, title: str, ingred: str, instruct: str) -> None:
        '''Update curr_recipe_text with current recipe for printing'''

        # Create separate function for this
        ingred = ingred.replace('\n', '\n- ')
        ingred = '- ' + ingred
        finstruct = ''
        count = 0
        ginstruct = '\n'.join(re.split(r'\d{0,2}\.[: \n\t:]', instruct))
        #finstruct = '\n'.join(re.split(r'.*\.[: \n\t:]$', instruct))
  
        for x in instruct.split('. '):
            count += 1
            temp = str(count) + '. ' + x + '\n'
            finstruct += temp

        if finstruct.count('\n') > ginstruct.count('\n'):
            format_instruct = finstruct
        else:
            format_instruct = ginstruct

        self.curr_recipe_text.setMarkdown(
            f'# {title}\n'
            f'## Ingredients\n'
            f'{ingred}\n'
            f'## Instructions:\n'
            f'{format_instruct }'
        )

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
    ui.createevents()  # Adding event listeners
    ui.linkimages(app)  # Link images to window
    ui.status_bar_display('Ready')
    # Set both our tab boxes to default and initialize keyboard shortcuts
    ui.tabWidgetRecipe.setCurrentIndex(0)
    ui.tabWidgetSearch.setCurrentIndex(0)
    ui.init_keyboard_shortcuts()
    ui.init_print()
    MainWindow.show()  # Finally, show the window
    if verbose:
        print('Initialized successfully and visible')
    sys.exit(app.exec())


if __name__ == '__main__':
    pass
