import pytest
from pathlib import Path
# from modules.recipe import Recipe
# from modules.recipelist import RecipeList
# from modules.psearch import p_search

# When testing, comment out above import blocks & uncomment below imports
from ACIT2911.modules.recipe import Recipe
from ACIT2911.modules.recipelist import RecipeList
from ACIT2911.modules.psearch import p_search

INGREDIENTS_LOWER = ["flour", "sugar", "butter"]
INGREDIENTS_UPPER = ["flOUr", "suGar", "buttER"]

@pytest.fixture
def recipelist():
    path = Path("./unit_tests/example_p.json")
    recipelist = RecipeList([path])
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
