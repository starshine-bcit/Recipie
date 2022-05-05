import pytest
from modules.recipe import Recipe
from modules.revent import MainWindowRecipie, return_rrecipe
# from ACIT2911.modules.recipe import Recipe                            #For local testing
# from ACIT2911.modules.revent import MainWindowRecipie, return_rrecipe #For local testing


RECIPE_LIST = [
    {
        "title": "Apple Pie",
        "ingredients": [
            "3 apples",
            "5 cups of flour",
            "2 cups of sugar",
            "10 sticks of butter"
        ],
        "instructions": "this is a recipe for apple pies"
    },
    {
        "title": "Blueberry Pie",
        "ingredients": [
            "2 cups of blueberries",
            "5 cups of flour",
            "2 cups of sugar",
            "10 sticks of butter"
        ],
        "instructions": "this is a recipe for blueberry pies"
    },
    {
        "title": "Death",
        "ingredients": [
            "3 cups of coca cola",
            "2 sticks of mentos"
        ],
        "instructions": "drink the cola then down the mentos"
    }
]


@pytest.fixture
def mw():
    mainwindow = MainWindowRecipie(True, RECIPE_LIST)
    return mainwindow


def test_main_window_methods(mw):
    """
    FIXME, need to look into the attributes and methods in the Qt copypasta
    """
    mw.random_button_click()

    pass
