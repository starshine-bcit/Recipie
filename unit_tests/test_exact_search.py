import pytest
from pathlib import Path
from modules.recipe import Recipe
from modules.recipelist import RecipeList
from modules.esearch import exact_search, e_search


USER_INPUT = ['flour', 'sugar', 'butter', 'apples']
ANNOYING_USER_INPUT = ['Flour', 'SUGAR', 'butTeR', 'blueBERRIES']
SINGULAR_USER_INPUT = ['Flour', 'sugar', 'Butter', 'apple']
ONION_ENJOYER_INPUT = ['bread', 'onion', 'ham', 'lettuce']
ONION_SOUP_ENJOYER_INPUT = ['bread', 'onion soup', 'ham', 'lettuce']
WEIRD_USER_INPUT = ['strawberry', 'chicken', 'broccoli']


@pytest.fixture
def rlist():
    path = Path("./unit_tests/example.json")
    recipelist = RecipeList([path])
    return recipelist


@pytest.fixture
def search(rlist):
    result = e_search(USER_INPUT, rlist)
    return result 


def test_exact_search(search):
    """
    Output should be a list
    Each item in the list should be a Recipe instance
    Capitalization shouldn't matter for the user input
    """
    #The first argument is the user's input, this user input is a list of ingredients, the second argument is the list of dictionaries
    assert isinstance(search, list) == True

    #To access the ingredients key inside the RECIPES_LIST, iterate over it and use .ingredients with the iterated dictionary eg.for recipe in RECIPE_LIST, if recipe['ingredients']...       


def test_exact_search_output_item(search):
    #The list should contain only dictionaries
    assert isinstance(search[0], Recipe) == True



def test_exact_search_working(search):
    #Checks if the exact match function worked, since only one item in the list matches those same ingredients
    assert search[0].name == "Apple Pie"  


def test_irregular_input(rlist):
    #Checks if the exact match function works even if the user doesn't know how to turn off their caps or stop holding shift
    result = e_search(ANNOYING_USER_INPUT, rlist)
    assert isinstance(result, list) == True
    assert result[0].name == "Blueberry Pie"


def test_plural_input(rlist):
    #Checks if the exact_search function works even if the user forgets to make the word plural
    result = e_search(SINGULAR_USER_INPUT, rlist)
    assert isinstance(result, list) == True
    assert result[0].name == "Apple Pie"


def test_exact_ingredient(rlist):
    #Checks if it only matches with the ingredient and not ingredients with that share the same ingredient, eg. onions and onion soup
    result = e_search(ONION_ENJOYER_INPUT, rlist)
    assert isinstance(result, list) == True
    assert len(result) == 1
    assert result[0].name == "Sandwich with Onions"


def test_exact_ingredient_two(rlist):
    #Checks if it only matches with the ingredient and not ingredients with that share the same ingredient, eg. onions and onion soup
    result = e_search(ONION_SOUP_ENJOYER_INPUT, rlist)
    assert isinstance(result, list) == True
    assert len(result) == 1
    assert result[0].name == "Onion Soup & Bread"


def test_main_search_using_categories_only(rlist):
    """
    Tests if main search works as intended using only categories
    """
    cat_search = exact_search([], ["nutfree", "lactosefree"], rlist)
    assert isinstance(cat_search, list) == True
    assert len(cat_search) == 3


def test_main_search_using_exact_search_only(rlist):
    """
    Tests if main search works as intended using only ingredients
    """
    search = exact_search(['flour', 'sugar', 'butter', 'apples'], [], rlist)
    assert isinstance(search, list) == True
    assert len(search) == 1


def test_main_search_using_both_searches(rlist):
    """
    Tests main search with both searches to narrow down searching for certain ingredients
    """
    search = exact_search(['flour', 'sugar', 'butter', 'apples'], ["vegetarian", "nutfree"], rlist)
    assert isinstance(search, list) == True
    assert len(search) == 1
    assert search[0].name == "Apple Pie"
