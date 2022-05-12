import pytest
# from modules.recipe import Recipe
# from modules.psearch import p_search

# When testing, comment out above import blocks & uncomment below imports
from ACIT2911.modules.recipe import Recipe
from ACIT2911.modules.psearch import p_search

INGREDIENTS_LOWER = ["flour", "sugar", "butter"]
INGREDIENTS_UPPER = ["flOUr", "suGar", "buttER"]

RECIPES = [
    {
        "title": "Apple Pie",
        "ingredients": [
            "5 cups of flour",
            "2 cups of sugar",
            "10 sticks of butter"
            "3 apples",
        ],
        "instructions": "this is a recipe for apple pies"
    },
    {
        "title": "Blueberry Pie",
        "ingredients": [
            "5 cups of flour",
            "2 cups of sugar",
            "10 sticks of butter"
            "2 cups of blueberries",
        ],
        "instructions": "this is a recipe for blueberry pies"
    },
    {
        "title": "Sweet Death",
        "ingredients": [
            "3 cups of coca cola",
            "2 sticks of mento",
            "1 cup of sugar"
        ],
        "instructions": "eat sugar, drink the cola, down the mentos"
    },
    {
        "title": "Fake Shortbread",
        "ingredients": [
            "2 cups butter",
            "1 cup packed salt",
            "4 1/2 cups all-purpose flour",
            "some mentos for fun"
        ],
        "instructions": "death by minty salt"
    }
]

# This searches for recipes that have flour, sugar, and butter as ingredients
@pytest.fixture
def results_list():
    """Fixture named results_list to hold p_search function return"""
    results_list = p_search(INGREDIENTS_LOWER, RECIPES)
    return results_list


# Check that function returns a list
def test_p_search(results_list):
    """Function should output a list"""
    assert isinstance(results_list, list) == True


# Check that items in the list are whole recipes (in dict format)
def test_p_search_list_item(results_list):
    """Function should return dictionary items in a list"""
    assert isinstance(results_list[0], dict) == True


# Expecting 2 recipes that match in results list
def test_p_search_length(results_list):
    """Function should return 2 items"""
    assert len(results_list) == 2


# Check that recipes in the results are correct
def test_p_search_correct_results(results_list):
    """Function should return these 2 recipes"""
    assert results_list[0]["title"] == 'Apple Pie'
    assert results_list[1]["title"] == 'Blueberry Pie'


# Check for case-insensitivity
def test_p_search_case_insensitive(results_list):
    """Function should work regardless of case for ingredients"""
    result = p_search(INGREDIENTS_UPPER, RECIPES)
    assert result == results_list


# Check for singular ingredient input vs plural in recipe
def test_p_search_singular():
    """Function should return recipe with pluralized ingredients
    e.g. input of 'apple' should match 'apples' in recipe ingredients.
    """
    result = p_search(['apple'], RECIPES)
    assert result[0]["title"] == 'Apple Pie'
