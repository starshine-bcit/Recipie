import pytest
import argparse
from unittest.mock import mock_open, patch
# from ACIT2911.modules.revent import MainWindowTest, parserecipe #For local testing
from modules.revent import MainWindowTest, parserecipe


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
    args = argparse.ArgumentParser()
    mainwindow = MainWindowRecipe(args, RECIPE_LIST)
    return mainwindow


def test_main_window_methods(mw):
    """
    FIXME, need to look into the attributes and methods in the Qt copypasta
    """
    
    pass


def test_parserecipe():
    parsed = parserecipe(RECIPE_LIST[0])
    assert [True for elem in parsed if type(elem) == str]


def test_main():
    pass
