import pytest
# from modules.esearch import ExactSearch
from ACIT2911.modules.esearch import exact_match

USER_INPUT = ['flour', 'sugar', 'butter', 'apples']
ANNOYING_USER_INPUT = ['Flour', 'SUGAR', 'butTeR', 'blueBERRIES']

RECIPES_LIST = [
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
def search():
    result = exact_match(USER_INPUT, RECIPES_LIST)
    return result 


def test_exact_search(search):
    """
    Output should be a list
    Each item in the list should be a Recipe instance
    Capitalization shouldn't matter for the user input
    """
    #The first argument is the user's input, this user input is a list of ingredients, the second argument is the list of dictionaries
    assert isinstance(search, list) == True

    #To access the ingredients key inside the RECIPES_LIST, iterate over it and use .ingredients with the iterated dictionary eg.for recipe in RECIPE_LIST, if recipe.ingredients...       


def test_exact_search_output_item(search):
    #The list should contain only dictionaries
    assert isinstance(search[0], dict) == True


def test_exact_search_working(search):
    #Checks if the exact match function worked, since only one item in the list matches those same ingredients
    assert search[0]['title'] == "Apple Pie"  


def test_irregular_input():
    #Checks if the exact match function works even if the user doesn't know how to turn off their caps or stop holding shift
    result = exact_search(ANNOYING_USER_INPUT, RECIPES_LIST)
    assert isinstance(result, list) == True
    assert result[0]['title'] == "Blueberry Pie"