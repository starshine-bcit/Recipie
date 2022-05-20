import pytest
from modules.catsearch import category_search, main_search


# simulates the Recipelist.recipes format
RLIST = [
    {
        "id": 1,
        "name": "Apple Pie",
        "ingredients": [
            "3 apples",
            "5 cups of flour",
            "2 cups of sugar",
            "10 sticks of butter"
        ],
        "instructions": "this is a recipe for apple pies",
        "diets": ["vegetarian", "nutfree"]
    },
    {
        "id": 2,
        "name": "Blueberry Pie",
        "ingredients": [
            "2 cups of blueberries",
            "5 cups of flour",
            "2 cups of sugar",
            "10 sticks of butter"
        ],
        "instructions": "this is a recipe for blueberry pies",
        "diets": ["vegetarian", "nutfree"]
    },
    {
        "id": 3,
        "name": "Death",
        "ingredients": [
            "3 cups of coca cola",
            "2 sticks of mentos",
            "2 nuts"
        ],
        "instructions": "drink the cola then down the mentos",
        "diets": ["lactosefree", "glutenfree", "vegan", "vegetarian"]
    },
    {
        "id": 4,
        "name": "Sandwich with Onions",
        "ingredients": [
            "2 slices of bread",
            "1 whole onion",
            "2 slices of ham",
            "1 lettuce leaf"
        ],
        "instructions": "Assemble this very sad sandwich that is meant to test the onion thingo",
        "diets": ["lactosefree", "nutfree"]
    },    
    {
        "id": 5,
        "name": "Onion Soup & Bread",
        "ingredients": [
            "1 can of onion soup",
            "3 slices of bread",
            "1 leg of ham",
            "1 whole head of lettuce"
        ],
        "instructions": "Toast the bread and drink the soup, eat like a barbarian.",
        "diets": ["lactosefree", "nutfree"]
    },
    {
        "id": 6,
        "name": "Weirdly Punctuated Recipe",
        "ingredients": [
            "2 grams of strawberries?",
            "1 spoonful of chicken!!!",
            "5 pounds of broccoli."
        ],
        "instruction": "Haha you thought this was a real recipe?!",
        "diets": ["nutfree", "glutenfree", "lactosefree"]
    }
]


def test_category_search():
    """
    Tests by giving a single category inside a list, should return a list of dictionaries that matches `nutfree`
    """
    search = category_search(["nutfree"], RLIST)
    assert isinstance(search, list) == True
    assert len(search) == 5


def test_category_search2():
    """
    tests for multiple categories, should return all recipes that have atleast both these cateories
    """
    search = category_search(["nutfree", "lactosefree"], RLIST)    
    assert isinstance(search, list) == True
    assert len(search) == 3
    assert isinstance(search[0], dict) == True


def test_main_search_using_categories_only():
    """
    Tests if main search works as intended using only categories
    """
    cat_search = main_search([], ["nutfree", "lactosefree"], RLIST)
    assert isinstance(cat_search, list) == True
    assert len(cat_search) == 3


def test_main_search_using_exact_search_only():
    """
    Tests if main search works as intended using only ingredients
    """
    search = main_search(['flour', 'sugar', 'butter', 'apples'], [], RLIST)
    assert isinstance(search, list) == True
    assert len(search) == 1


def test_main_search_using_both_searches():
    """
    Tests main search with both searches to narrow down searching for certain ingredients
    """
    search = main_search(['flour', 'sugar', 'butter', 'apples'], ["vegetarian", "nutfree"], RLIST)
    assert isinstance(search, list) == True
    assert len(search) == 1
    assert search[0]['name'] == "Apple Pie"  