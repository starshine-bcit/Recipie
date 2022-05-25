import pytest
from pathlib import Path
from modules.catsearch import category_search
from modules.recipelist import RecipeList
from modules.recipe import Recipe
from modules.revent import ProgressCallback


@pytest.fixture
def callback():
    cb = ProgressCallback()

    return cb


@pytest.fixture
def rlist(callback):
    path = Path("./unit_tests/example.json")
    recipelist = RecipeList([path], callback)
    return recipelist


def test_category_search(rlist):
    """
    Tests by giving a single category inside a list, should return a list of dictionaries that matches `nutfree`
    """
    search = category_search(["nutfree"], rlist)
    assert isinstance(search, list) == True
    assert len(search) == 5


def test_category_search2(rlist):
    """
    tests for multiple categories, should return all recipes that have atleast both these cateories
    """
    search = category_search(["nutfree", "lactosefree"], rlist)    
    assert isinstance(search, list) == True
    assert len(search) == 3
    assert isinstance(search[0], Recipe) == True
