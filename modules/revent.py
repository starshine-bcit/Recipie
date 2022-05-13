'''Recipie module for subclassing and event handling'''
import sys
import traceback
import re
import json
from pathlib import Path
from random import choice

from PyQt6 import QtCore, QtGui, QtWidgets, QtPrintSupport

from .qtui import Ui_MainWindow
from .recipelist import RecipeList
from .recipe import Recipe
from .recipewindow import Ui_Dialog
from .esearch import exact_search
from .psearch import p_search


# Credits to https://www.pythonguis.com for this code
class WorkerSignals(QtCore.QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = QtCore.pyqtSignal()
    # error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(list)
    progress = QtCore.pyqtSignal(int)


class Worker(QtCore.QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.setAutoDelete(True)

        # Add the callback to our kwargs
        # self.kwargs['progress_callback'] = self.signals.progress

    @QtCore.pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            print((exctype, value, traceback.format_exc()))
            # self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done
#End credited code here



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
        self.currname = ''
        self.multiwin = {} 
        #self.timer = QtCore.QTimer()
        #self.timer.setInterval(1000)
        #self.timer.timeout.connect(self.recurring_timer)
        #self.timer.start()

    def setupUicustom(self):
        '''Setup various elements which have no depends'''

        self.printer = QtPrintSupport.QPrinter()
        self.curr_recipe_md = QtGui.QTextDocument()
        self.labelStatusBarRecipeCount = QtWidgets.QLabel(
            f'Indexing {len(self.rlist.recipes)} recipes ')
        self.statusbar.addPermanentWidget(self.labelStatusBarRecipeCount)
        self.statusbar.showMessage('Ready')
        self.tabWidgetRecipe.setCurrentIndex(0)
        self.tabWidgetSearch.setCurrentIndex(0)
        self.pushButtonDisplayRecipeNewWindow.setEnabled(False)
        self.quotes = load_quotes()
        self.threadpool = QtCore.QThreadPool().globalInstance()

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
        self.pushButtonRemoveSelected.clicked.connect(
            self.remove_selected_search)
        self.pushButtonResetSearch.clicked.connect(self.reset_search)
        self.pushButtonRecipeClear.clicked.connect(self.clear_recipe_display)
        self.actionPrint.triggered.connect(self.call_print)
        self.listWidgetSearchResults.itemDoubleClicked.connect(
            self.click_search_result)
        self.pushButtonDisplayRecipeNewWindow.clicked.connect(
            self.display_recipe_window)
        self.radioButtonExclusive.clicked.connect(self.exclusive_search_clicked)
        self.radioButtonInclusive.clicked.connect(self.inclusive_search_clicked)

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
            print(f'Selecting random recipe {rrecipe.name} and displaying...')

        self.display_quote()
        self.display_recipe(rrecipe)

    def display_recipe(self, rcp: Recipe) -> None:
        '''Display chosen recipe in the main window'''

        ingreds = rcp.ingredients_as_str()

        self.labelRecipeName.setText(rcp.name)
        self.textBrowserRecipeIngredients.setText(ingreds)
        self.textBrowserRecipeDirections.setText(rcp.instructions)
        self.set_md_recipe(rcp.name, ingreds, rcp.instructions)
        self.pushButtonDisplayRecipeNewWindow.setEnabled(True)
        self.currname = rcp.name

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
        search_terms = [self.listWidgetSearchInput.item(
            x).text() for x in range(self.listWidgetSearchInput.count())]
        if stext == '' and len(search_terms) == 0:
            print('Error, you can\'t search for nothing fool')
        elif stext == '' and len(search_terms) > 0:
            self.call_search()
        elif stext in search_terms:
            self.lineEditIngredientEntry.setText('')
            if self.verbose: print('Error, search term already exists')
        else:
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
        # Pass the function to execute
        if len(search_terms) > 0:
            if self.radioButtonExclusive.isChecked():
                if self.verbose: print('Starting exclusive search...')
                self.searchworker = Worker(exact_search, search_terms, self.rlist)
                self.lock_ui_elements()
                # progress_callback.emit(n*100/4)
                #search_type = getattr(esearch, 'exact_search')
            elif self.radioButtonInclusive.isChecked():
                if self.verbose: print('Starting inclusive search...')
                self.searchworker = Worker(p_search, search_terms, self.rlist)
                self.lock_ui_elements()
                #search_type = getattr(exact_search, 'partial_search')

             # Setup our signals
            self.searchworker.signals.result.connect(self.display_search_result_list)
            self.searchworker.signals.finished.connect(self.thread_complete)
            # searchworker.signals.progress.connect(self.progress_fn)

            # Execute our search
            self.threadpool.start(self.searchworker)
        else:
            self.srlist.clear()
            if self.verbose:
                print('Search called, but no items to search for')
 
    def thread_complete(self):
        if self.verbose: print('Search thread completed')
        self.unlock_ui_elements()

    def lock_ui_elements(self):
        '''Lock search-related ui elements'''

        self.lineEditIngredientEntry.setText('Patience, grasshopper')
        self.lineEditIngredientEntry.setEnabled(False)
        self.commandLinkButtonEnterIngredient.setEnabled(False)
        self.radioButtonExclusive.setEnabled(False)
        self.radioButtonInclusive.setEnabled(False)
        self.pushButtonResetSearch.setEnabled(False)
        self.pushButtonRemoveSelected.setEnabled(False)
        self.actionRemove_Selected.setEnabled(False)
        self.actionReset_Search.setEnabled(False)
        self.status_bar_display('Searching...')

    def unlock_ui_elements(self):
        ''''Unlock search-related ui elements'''

        self.lineEditIngredientEntry.setEnabled(True)
        self.lineEditIngredientEntry.setText('')
        self.commandLinkButtonEnterIngredient.setEnabled(True)
        self.radioButtonExclusive.setEnabled(True)
        self.radioButtonInclusive.setEnabled(True)
        self.pushButtonResetSearch.setEnabled(True)
        self.pushButtonRemoveSelected.setEnabled(True)
        self.actionRemove_Selected.setEnabled(True)
        self.actionReset_Search.setEnabled(True)

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
        self.pushButtonDisplayRecipeNewWindow.setEnabled(False)
        self.labelTopBarText.setText('Welcome to Recipie Beta, please hit \'Random Recipe to try it out!')
        if self.verbose:
            print('Clearing displayed recipe...')

    def call_print(self) -> None:
        '''Open print dialogue for current selected recipe'''

        self.print_dialog = QtPrintSupport.QPrintDialog(self.printer)
        self.print_dialog.open(self.send_print)

    def send_print(self) -> None:
        '''Send document to configured printer'''

        self.curr_recipe_md.print(self.printer)

    def set_md_recipe(self, title: str, ingred: str, instruct: str) -> None:
        '''Format and store markdown based on string version of recipe

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

    def display_search_result_list(self, unlist: list[Recipe]) -> None:
        '''Displays list of recipes in search bar'''

        self.srlist.clear()

        for x in range(len(unlist)):
            self.srlist.update({x: unlist[x]})
        srlistlen = len(self.srlist)

        for x in range(srlistlen):
            newname = self.srlist[x].name
            newitem = QtWidgets.QListWidgetItem(newname)
            self.listWidgetSearchResults.addItem(newitem)

        self.status_bar_display(f'Found {srlistlen} results')
        if self.verbose:
            print(f'Successfully searched and found {srlistlen} results')
        self.tabWidgetRecipe.setCurrentIndex(1)

    def click_search_result(self) -> None:
        '''Display search result when clicked on'''

        currindex = self.listWidgetSearchResults.currentRow()
        self.display_recipe(self.srlist[currindex])
        self.tabWidgetRecipe.setCurrentIndex(0)
        if self.verbose:
            print(f'Display recipe at index {currindex}')

    def display_recipe_window(self) -> None:
        '''Display recipe in new window'''

        self.multiwin[self.currname] = QtWidgets.QDialog()
        self.multiwin[self.currname + '2'] = Ui_Dialog()
        self.multiwin[self.currname +
                      '2'].setupUi(self.multiwin[self.currname])
        self.multiwin[self.currname].setWindowTitle(self.currname)
        self.multiwin[self.currname +
                      '2'].textBrowserDisplay.setMarkdown(self.curr_recipe_md.toMarkdown())
        self.multiwin[self.currname].show()

    def display_quote(self) -> None:
        '''Display quotes from self.quotes'''

        rquote = choice(self.quotes['quotes'])
        qstring = rquote['quote'] + '\n- ' + rquote['author']
        self.labelTopBarText.setText(qstring)

    def exclusive_search_clicked(self) -> None:
        self.radioButtonExclusive.setChecked(True)
        self.radioButtonInclusive.setChecked(False)
        self.call_search()

    def inclusive_search_clicked(self) -> None:
        self.radioButtonExclusive.setChecked(False)
        self.radioButtonInclusive.setChecked(True)
        self.call_search()

def load_quotes():
    """Load quotes from hardcoded json file

    Returns:
        dict: dictionary of quotes
    """    
    try:
        file = Path('./data/quotes/quotes.json')
        with file.open('r', encoding='utf-8') as fp:
            data = json.load(fp)
        return data
    except FileNotFoundError as err: print(err)
    except TypeError as err: print(err)


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
