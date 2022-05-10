import pytest
from modules.recipe import Recipe
from modules import psearch

INGREDIENTS = ["flour", "sugar", "butter"]

RECIPES = [
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

def test_partial_search():

    # Searching for recipes that have flour, sugar, and butter as ingredients
    results_list = psearch.p_search(INGREDIENTS, RECIPES)
    
    # Check that function returns a list
    assert isinstance(results_list, list) == True

    # Expecting 2 recipes that match in results list
    assert len([results_list]) == 2

    # Check that items in the list are Recipe instances
    assert isinstance(results_list[0], Recipe) == True
