import pytest
from pathlib import Path
from modules.recipe import Recipe
from modules.recipelist import RecipeList
from modules.revent import MainWindowRecipie

# from ACIT2911.modules.recipe import Recipe            #For local testing
# from ACIT2911.modules.recipelist import RecipeList    #For local testing
# from ACIT2911.modules.revent import MainWindowRecipie #For local testing


@pytest.fixture
def rlist():
    """Creates a RecipeList instance, uses the example.json located in the same folder

    Returns:
        recipelist (RecipeList): a RecipeList instance, uses RECIPE_JSON as its datastore
    """
    path = Path("./unit_tests/example.json")
    recipelist = RecipeList([path])
    return recipelist


@pytest.fixture
def mw(rlist):
    mainwindow = MainWindowRecipie(True, rlist)
    return mainwindow


def test_main_window_recipie(mw):
    assert isinstance(mw.rlist, RecipeList) == True
    assert mw.verbose == True


# def test_mwr_methods(mw):
#     mw.random_button_click()
#     pass
