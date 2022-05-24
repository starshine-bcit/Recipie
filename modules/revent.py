'''Recipie module for subclassing and event handling'''
from functools import singledispatch
import sys
import traceback
import re
import json
from pathlib import Path
from random import choice
import operator
import csv

from PyQt6 import QtCore, QtGui, QtWidgets, QtPrintSupport

from .qtui import Ui_MainWindow
from .recipelist import RecipeList
from .recipe import Recipe
from .recipewindow import Ui_Dialog
from .loadingbar import Ui_DialogLoading
from .esearch import exact_search
from .psearch import partial_search

#####################################################
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
            # Return the result of the processing
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()  # Done


# End credited code here
#####################################################

class LoadWorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    result = QtCore.pyqtSignal(RecipeList)
    progress = QtCore.pyqtSignal(int)


class LoadWorker(QtCore.QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(LoadWorker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = LoadWorkerSignals()
        self.setAutoDelete(True)

    @QtCore.pyqtSlot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            print((exctype, value, traceback.format_exc()))
            # self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class LoadingWindow(Ui_DialogLoading):
    def __init__(self) -> None:
        super().__init__()

    def update_progress_bar(self, pct: int) -> None:
        self.progressBar.setValue(pct)

    def update_loading_message(self, msg: str) -> None:
        self.labelLoadingMessage.setText(msg)


class ProgressCallback(QtCore.QObject):
    progressChanged = QtCore.pyqtSignal(int)

    def __call__(self, value):
        self.progressChanged.emit(value)


class MainWindowRecipie(Ui_MainWindow):
    """Main Window of Recipie, sub-classed from qtui.Ui_MainWindow
        Contains a variety of functions and methods to manipulate UI

    Args:
        Ui_MainWindow (Ui_MainWindow): Ui_MainWindow class to subclass off of

    Attributes:
        rlist (RecipeList): Main working RecipeList instance
        verbose (bool): Enables logging useful messages to console
    """

    def __init__(self, verbose: bool, dspath: list[Path], mw: QtWidgets.QMainWindow, app: QtWidgets.QApplication) -> None:
        """Initialize this instance with provided args
        Use super().__init__() just in case

        Args:
            verbose (bool): True enables logging to console
            rlist (RecipeList): Instance of RecipeList with all recipes
        """

        super().__init__()
        self.srlist = {}
        self.verbose = verbose
        self.currname = ''
        self.currid = ''
        self.multiwin = {}
        self.favlist = []
        self.cats = []
        self.mw = mw
        self.dspath = dspath
        self.app = app
        self.setupUi(self.mw)
        self.load_widget = QtWidgets.QDialog()
        self.load_display = LoadingWindow()
        self.threadpool = QtCore.QThreadPool().globalInstance()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.linkimages(self.app)
        self.run_loading_window()
        sys.exit(self.app.exec())

    def run_loading_window(self) -> None:
        '''Display our loading window and calls worker to parse json recipes'''

        callback = ProgressCallback()
        self.load_display.setupUi(self.load_widget)
        self.load_display.update_progress_bar(0)
        self.load_widget.setWindowTitle('Loading recipie...')
        self.load_widget.show()
        self.loadworker = LoadWorker(self.create_recipe_list, callback)
        self.loadworker.signals.result.connect(self.assign_rcp_list)
        self.loadworker.signals.finished.connect(self.run_loading_finished)
        callback.progressChanged.connect(self.load_display.update_progress_bar)
        self.threadpool.start(self.loadworker)

    def create_recipe_list(self, callback) -> None:
        rlist = RecipeList(self.dspath, callback)
        return rlist

    def assign_rcp_list(self, rlist: RecipeList):
        self.rlist = rlist

    def run_loading_finished(self) -> None:
        self.load_widget.hide()
        self.setupUicustom()
        self.createevents()
        self.mw.show()

    def setupUicustom(self):
        '''Setup various elements which have no depends'''

        self.printer = QtPrintSupport.QPrinter()
        self.curr_recipe_md = QtGui.QTextDocument()
        if self.verbose:
            print(f'Total recipes indexed: {len(self.rlist.recipes)}')
        self.labelStatusBarRecipeCount = QtWidgets.QLabel(
            f'Indexing {len(self.rlist.recipes)} recipes ')
        self.statusbar.addPermanentWidget(self.labelStatusBarRecipeCount)
        self.labelStatusBarFavCount = QtWidgets.QLabel()
        self.update_favcount_status_bar()
        self.statusbar.addPermanentWidget(self.labelStatusBarFavCount)
        self.statusbar.showMessage('Ready')
        self.tabWidgetRecipe.setCurrentIndex(0)
        self.tabWidgetSearch.setCurrentIndex(0)
        self.pushButtonDisplayRecipeNewWindow.setEnabled(False)
        self.pushButtonAddFavourite.setEnabled(False)
        self.quotes = load_quotes()
        self.pushButtonRemoveAllFavourites.setEnabled(False)
        self.pushButtonRemoveSelectedFavourites.setEnabled(False)
        self.load_favourites_from_file()
        self.listWidgetFavouriteRecipes.setSortingEnabled(True)

        # self.listWidgetSearchResults.setSortingEnabled(True)
        # Enable this once we have id on recipes?

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
        self.radioButtonExclusive.clicked.connect(
            self.call_search)
        self.radioButtonInclusive.clicked.connect(
            self.call_search)
        self.pushButtonAddFavourite.clicked.connect(self.add_favourite)
        self.pushButtonRemoveAllFavourites.clicked.connect(
            self.remove_all_favourites)
        self.pushButtonRemoveSelectedFavourites.clicked.connect(
            self.remove_selected_favourites)
        self.listWidgetFavouriteRecipes.itemDoubleClicked.connect(
            self.display_recipe_from_favourites)
        self.timer.timeout.connect(self.timeout_status_bar_display)
        self.pushButtonResetFilters.clicked.connect(self.clear_cats_list)
        self.checkBoxGluten.clicked.connect(self.update_cats_list)
        self.checkBoxLactose.clicked.connect(self.update_cats_list)
        self.checkBoxNut.clicked.connect(self.update_cats_list)
        self.checkBoxVegan.clicked.connect(self.update_cats_list)
        self.checkBoxVegetarian.clicked.connect(self.update_cats_list)
        self.pushButtonSendFilterSearch.clicked.connect(self.call_search)

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
        self.pushButtonAddFavourite.setEnabled(True)
        self.currname = rcp.name
        self.currid = rcp.id
        self.currrcp = rcp

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
            if self.verbose:
                print('Error, search term already exists')
        else:
            self.lineEditIngredientEntry.setText('')
            newitem = QtWidgets.QListWidgetItem(stext)
            self.listWidgetSearchInput.addItem(newitem)
            self.call_search()

    def call_search(self) -> None:
        '''Sends list of user search terms to logic search functions'''

        self.listWidgetSearchResults.clear()
        if self.listWidgetSearchInput.count() > 0:
            search_terms = [self.listWidgetSearchInput.item(
                x).text() for x in range(self.listWidgetSearchInput.count())]
        else:
            search_terms = []
        if self.verbose:
            print(
                f'Sending these terms to search:\n{search_terms}'
                f'Sending these categories to search:\n{self.cats}'
            )
        # Pass the function to execute
        if len(search_terms) > 0 or len(self.cats) > 0:
            if self.radioButtonExclusive.isChecked():
                if self.verbose:
                    print('Starting exclusive search...')
                self.searchworker = Worker(
                    exact_search, search_terms, self.cats, self.rlist)
                self.lock_ui_elements()
                # progress_callback.emit(n*100/4)
            elif self.radioButtonInclusive.isChecked():
                if self.verbose:
                    print('Starting inclusive search...')
                self.searchworker = Worker(
                    partial_search, search_terms, self.cats, self.rlist)
                self.lock_ui_elements()

             # Setup our signals
            self.searchworker.signals.result.connect(
                self.display_search_result_list)
            self.searchworker.signals.finished.connect(self.thread_complete)
            # searchworker.signals.progress.connect(self.progress_fn)

            # Execute our search
            self.threadpool.start(self.searchworker)
        else:
            self.srlist.clear()
            if self.verbose:
                print('Error: Search called, there are no terms or categories')

    def load_progress_callback(self) -> None:
        '''Updates UI progress bar as program loads'''
        pass

    def thread_complete(self):
        '''To be triggered when search worker finishes, unlocks ui elements'''

        if self.verbose:
            print('Search thread completed')
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
        self.pushButtonSendFilterSearch.setEnabled(False)
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
        self.pushButtonSendFilterSearch.setEnabled(True)
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
        self.pushButtonAddFavourite.setEnabled(False)
        self.labelTopBarText.setText(
            'Welcome to Recipie Beta, please hit \'Random Recipe to try it out!')
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
        This code could use a refactor

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

        unlist.sort(key=operator.attrgetter('name'))

        for x in range(len(unlist)):
            self.srlist.update({x: unlist[x]})
        srlistlen = len(self.srlist)

        for x in range(srlistlen):
            #newname = self.get_list_recipe_text(self.srlist[x].name, self.srlist[x].id)
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
        qstring = rquote['quote'] + ' -- ' + rquote['author']
        self.labelTopBarText.setText(qstring)

    def load_favourites_from_file(self) -> None:
        '''Load saved and favourited recipes from hardcoded csv file'''

        favfilepath = Path(__file__).parent.parent.joinpath(
            'data/favourites.csv')
        if favfilepath.exists():
            with favfilepath.open('r', encoding='utf-8', newline='') as file:
                reader = csv.reader(file, delimiter='~', quotechar='`')
                tlist = list(reader)
                self.favlist = tlist[0]
                if len(self.favlist) > 0:
                    self.pushButtonRemoveAllFavourites.setEnabled(True)
                    self.pushButtonRemoveAllFavourites.setEnabled(True)
                self.display_favourites_list()
                if self.verbose:
                    print(f'Loaded {len(self.favlist)} favourites from file')
        else:
            if self.verbose:
                print(f'No favourites file to load :\'(')
            self.favlist = []
        self.update_favcount_status_bar()

    def write_favourites_to_file(self) -> None:
        '''Write out a csv file of favourited recipes'''

        favfilepath = Path(__file__).parent.parent.joinpath(
            'data/favourites.csv')
        if len(self.favlist) > 0:
            with favfilepath.open('w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file, delimiter='~', quotechar='`')
                writer.writerow(self.favlist)
            if self.verbose:
                print(
                    f'Successfully wrote favourites file with {len(self.favlist)} items')
        else:
            if favfilepath.is_file:
                if self.verbose:
                    print('Deleting favourites file')
                favfilepath.unlink()
        self.update_favcount_status_bar()

    def add_favourite(self) -> None:
        '''Add selected recipe from search to favourites'''

        if self.currname in self.favlist:
            if self.verbose:
                print('Error: Recipe is already in favourites')
        else:
            if self.verbose:
                print(f'Added favourite recipe: {self.currname}')
            newname = self.get_list_recipe_text(self.currname, self.currid)
            self.favlist.append(newname)
            self.write_favourites_to_file()
            self.display_favourites_list()
            self.status_bar_display('Added favourite')
            self.timer.singleShot(1500, self.timeout_status_bar_display)

    def get_list_recipe_text(self, name: str, id: int) -> str:
        '''Sets display text for favourites and search results'''

        return name + ' -- ID: ' + str(id)

    def parse_list_recipe_text(self, intext: str) -> int:
        '''Parses display text for favourites and search results
        Returns and integer corresponding to recipe id'''

        try:
            ind = intext.find(' -- ID: ')
            return int(intext[ind+8::])
        except (ValueError, IndexError, TypeError) as err:
            if self.verbose:
                print('Error:', err)
            return 0

    def display_favourites_list(self) -> None:
        '''Reset then display all favourited recipes'''

        if len(self.favlist) > 0:
            self.listWidgetFavouriteRecipes.clear()
            for x in self.favlist:
                newitem = QtWidgets.QListWidgetItem(x)
                self.listWidgetFavouriteRecipes.addItem(newitem)
            self.pushButtonRemoveAllFavourites.setEnabled(True)
            self.pushButtonRemoveSelectedFavourites.setEnabled(True)
            if self.verbose:
                print(f'Displaying {len(self.favlist)} favourites')
        else:
            self.pushButtonRemoveAllFavourites.setEnabled(False)
            self.pushButtonRemoveSelectedFavourites.setEnabled(False)

    def display_recipe_from_favourites(self) -> None:
        '''Find favourited recipe and display it as normal'''

        rname = self.listWidgetFavouriteRecipes.currentItem().text()
        clickedid = self.parse_list_recipe_text(rname)
        found = False
        for recipe in self.rlist.recipes:
            if recipe.id == clickedid:
                rmatch = recipe
                found = True
                break
        if found:
            if self.verbose:
                print('Found favourite recipe to display')
            self.display_recipe(rmatch)
            self.tabWidgetRecipe.setCurrentIndex(0)
        else:
            if self.verbose:
                print('Error: Can\'t find favourite recipe to display')

    def remove_all_favourites(self) -> None:
        '''Remove all favourites and clear file'''

        # Add dialog box to confirm
        self.listWidgetFavouriteRecipes.clear()
        self.favlist.clear()
        self.pushButtonRemoveAllFavourites.setEnabled(False)
        self.pushButtonRemoveSelectedFavourites.setEnabled(False)
        if self.verbose:
            print('Removing all favourites')
        self.write_favourites_to_file()

    def remove_selected_favourites(self) -> None:
        '''Remove favourites as selected on list widget'''

        count = len(self.listWidgetFavouriteRecipes.selectedItems())
        if count > 0:
            for listitem in self.listWidgetFavouriteRecipes.selectedItems():
                self.favlist.remove(listitem.text())
                self.listWidgetFavouriteRecipes.takeItem(
                    self.listWidgetFavouriteRecipes.row(listitem))
                self.write_favourites_to_file()
                if self.verbose:
                    print(f'Removed {count} items from favourites')
            if self.listWidgetFavouriteRecipes.count() == 0:
                self.pushButtonRemoveAllFavourites.setEnabled(False)
                self.pushButtonRemoveSelectedFavourites.setEnabled(False)
        else:
            if self.verbose:
                print('No selected favourites to remove')

    def timeout_status_bar_display(self) -> None:
        '''Function to trigger Ready display when timer runs out'''

        self.status_bar_display('Ready')

    def update_favcount_status_bar(self) -> None:
        self.labelStatusBarFavCount.setText(
            f'Favourites: {len(self.favlist)} ')

    def update_cats_list(self) -> None:
        '''Updates cats list on checkbox clicks'''

        tcats = []
        if self.checkBoxGluten.isChecked():
            tcats.append('glutenfree')
        if self.checkBoxLactose.isChecked():
            tcats.append('lactosefree')
        if self.checkBoxNut.isChecked():
            tcats.append('nutfree')
        if self.checkBoxVegan.isChecked():
            tcats.append('vegan')
        if self.checkBoxVegetarian.isChecked():
            tcats.append('vegetarian')
        self.cats = tcats
        if self.verbose:
            print(f'Updated cats list is:\n{self.cats}')

    def clear_cats_list(self) -> None:
        '''Clears all checkboxes for diets and associated list'''

        self.checkBoxGluten.setChecked(False)
        self.checkBoxLactose.setChecked(False)
        self.checkBoxNut.setChecked(False)
        self.checkBoxVegan.setChecked(False)
        self.checkBoxVegetarian.setChecked(False)
        self.cats.clear()
        if self.verbose:
            print('Cleared cats list')


def load_quotes():
    '''Load quotes from hardcoded json file'''

    try:
        file = Path(__file__).parent.parent.joinpath('data/quotes/quotes.json')
        with file.open('r', encoding='utf-8') as fp:
            data = json.load(fp)
        return data
    except FileNotFoundError as err:
        print(err)
    except TypeError as err:
        print(err)


def initmainwindow(verbose: bool, dspath: list[Path]) -> None:
    '''Initialize and display main recipie window

        Args:
            verbose (bool): Specify verbose setting for program
            rlist (RecipeList): Main instance of RecipeList
    '''

    if verbose:
        print('Starting to initialize ui...')
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowRecipie(verbose, dspath, MainWindow, app)


if __name__ == '__main__':
    pass
