import pytest
from pathlib import Path
from modules.recipe import Recipe
from modules.recipelist import RecipeList
from modules.psearch import p_search, partial_search
from modules.revent import ProgressCallback


INGREDIENTS_LOWER = ["flour", "sugar", "butter"]
INGREDIENTS_UPPER = ["flOUr", "suGar", "buttER"]


@pytest.fixture
def callback():
    cb = ProgressCallback()

    return cb


@pytest.fixture
def recipelist(callback):
    path = Path("./unit_tests/example_p.json")
    recipelist = RecipeList([path], callback)
    return recipelist

# This searches for recipes that have flour, sugar, and butter as ingredients
@pytest.fixture
def results_list(recipelist):
    """Fixture named results_list to hold p_search function return"""
    results_list = p_search(INGREDIENTS_LOWER, recipelist)
    return results_list


# Check that function returns a list
def test_p_search(results_list):
    """Function should output a list"""
    assert isinstance(results_list, list) == True


# Check that items in the list are Recipe instances
def test_p_search_list_item(results_list):
    """Function should return Recipe items in a list"""
    assert isinstance(results_list[0], Recipe) == True


# Expecting 2 recipes that match in results list
def test_p_search_length(results_list):
    """Function should return 2 items"""
    assert len(results_list) == 2


# Check that recipes in the results are correct
def test_p_search_correct_results(results_list):
    """Function should return these 2 recipes"""
    assert results_list[0].name == 'Apple Pie'
    assert results_list[1].name == 'Blueberry Pie'


# Check for case-insensitivity
def test_p_search_case_insensitive(recipelist, results_list):
    """Function should work regardless of case for ingredients"""
    result = p_search(INGREDIENTS_UPPER, recipelist)
    assert result == results_list


# Check for singular ingredient input vs plural in recipe
def test_p_search_singular(recipelist):
    """Function should return recipe with pluralized ingredients
    e.g. input of 'apple' should match 'apples' in recipe ingredients.
    """
    result = p_search(['apple'], recipelist)
    assert result[0].name == 'Apple Pie'


def test_main_search_using_categories_only(recipelist):
    """
    Tests if main search works as intended using only categories
    """
    cat_search = partial_search([], ["nutfree", "lactosefree"], recipelist)
    assert isinstance(cat_search, list) == True
    assert len(cat_search) == 2
    assert cat_search[1].name == "Sweet Death"



def test_main_search_using_partial_search_only(recipelist):
    """
    Tests if main search works as intended using only ingredients
    """
    search = partial_search(['flour', 'sugar', 'butter', 'apples'], [], recipelist)
    assert isinstance(search, list) == True
    assert len(search) == 1


def test_main_search_using_both_searches(recipelist):
    """
    Tests main search with both searches to narrow down searching for certain ingredients
    """
    search = partial_search(['flour', 'sugar', 'butter', 'apples'], ["vegetarian", "nutfree"], recipelist)
    assert isinstance(search, list) == True
    assert len(search) == 1
    assert search[0].name == "Apple Pie"  
