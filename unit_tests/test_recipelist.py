import pytest
from unittest.mock import mock_open, patch
from modules.recipe import Recipe
from modules.recipelist import RecipeList
# from ACIT2911.modules.recipe import Recipe            #For local testing
# from ACIT2911.modules.recipelist import RecipeList    #For local testing


RECIPE_JSON = """{
    "asdfoisdnfoisdf": {
        "title": "Apple Pie",
        "ingredients": [
            "3 apples",
            "5 cups of flour",
            "2 cups of sugar",
            "10 sticks of butter"
        ],
        "instructions": "this is a recipe for apple pies"
    },
    "asdojsdnsdf": {
        "title": "Blueberry Pie",
        "ingredients": [
            "2 cups of blueberries",
            "5 cups of flour",
            "2 cups of sugar",
            "10 sticks of butter"
        ],
        "instructions": "this is a recipe for blueberry pies"
    },
    "asodfndsofnsdf": {
        "title": "Death",
        "ingredients": [
            "3 cups of coca cola",
            "2 sticks of mentos"
        ],
        "instructions": "drink the cola then down the mentos"
    }
}"""

INGREDIENTS = ("Apple", "Orange", "flour", "SUGAR", "bUttER")


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=RECIPE_JSON)
def rlist(mock_file):
    """Creates a RecipeList instance, mocks a JSON for it to open on initialisation

    Args:
        mock_file (JSON): the RECIPE_JSON above

    Returns:
        recipelist (RecipeList): a RecipeList instance, uses RECIPE_JSON as its datastore
    """
    recipelist = RecipeList()
    return recipelist


def test_recipe_list(rlist):
    """Test RecipeList class, checks if it calls and reads the json appropriately

    Args:
        rlist (RecipeList): A RecipeList instance
    """
    # Opens the datastore
    assert rlist.call_count == 1

    # Checks if we're reading the datastore
    assert rlist.call_args[0][0] == "r"

    assert len(rlist.recipes) == 3
    assert type(rlist.recipes) == list
    assert (rlist.recipes[0], ) == True


def test_not_recipe_list():
    """
    Checks for errors if no datastore is given
    """
    with pytest.raises(FileNotFoundError):
        not_rlist = RecipeList()


def test_recipe_list_methods(rlist):
    """
    Test the RecipeList methods
    - sort_ingredients
    - get_random_recipe

    Args:
        rlist (RecipeList): RecipeList instance
    """
#     # get a list of recipes back
#     recipes = rlist.get_recipes()
#     assert isinstance(recipes, list)
#     assert len(recipes) == 3

    # get a random recipe, should only be a single recipe
    random_recipe = rlist.get_random_recipe()
    assert len(random_recipe) == 1
    assert isinstance(random_recipe, Recipe) == True

#     # get a list of recipes back, based on ingredients
#     # capitalization shouldn't matter on the user's end
#     ingr_recipes = rlist.by_ingredients(INGREDIENTS)
#     for i in ingr_recipes[0]['ingredients']:
#         assert i in INGREDIENTS
