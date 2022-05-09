'''Recipie module for subclassing and event handling'''
import sys

from PyQt6 import QtCore, QtGui, QtWidgets

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
        self.display_recipe(
            rrecipe.name, ingreds, rrecipe.instructions)

    def display_recipe(self, title: str, ingred: str, instruct: str) -> None:
        '''Display chosen recipe in the main window'''

        self.labelRecipeName.setText(title)
        self.textBrowserRecipeIngredients.setText(ingred)
        self.textBrowserRecipeDirections.setText(instruct)

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


def initmainwindow(verbose, rlist: RecipeList) -> None:
    '''Initialize and display main recipie window

        Args:
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
    MainWindow.show()
    if verbose:
        print('Initialized successfully and visible')
    sys.exit(app.exec())


if __name__ == '__main__':
    pass
