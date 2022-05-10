# from modules.esearch import ExactSearch
from ACIT2911.modules import esearch
from ACIT2911.modules.recipe import Recipe

USER_INPUT = ['Flour', 'SUGAR', 'butter', 'apPPle']

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


def test_exact_search():
    """
    Output should be a list
    Each item in the list should be a Recipe instance
    Capitalization shouldn't matter for the user input
    """
    result = esearch(USER_INPUT)
    assert isinstance(result, list) == True
    assert isinstance(result[0], Recipe) == True
    assert result.title == "Apple Pie"