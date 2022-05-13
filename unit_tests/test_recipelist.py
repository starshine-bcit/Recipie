import pytest
from pathlib import Path
from modules.recipe import Recipe
from modules.recipelist import RecipeList

# from ACIT2911.modules.recipe import Recipe            #For local testing
# from ACIT2911.modules.recipelist import RecipeList    #For local testing


INGREDIENTS = ("Apple", "Orange", "flour", "SUGAR", "bUttER")


@pytest.fixture
def rlist():
    """Creates a RecipeList instance, uses the example.json located in the same folder

    Returns:
        recipelist (RecipeList): a RecipeList instance, uses RECIPE_JSON as its datastore
    """
    path = Path("./unit_tests/example.json")
    recipelist = RecipeList([path])
    return recipelist


def test_recipe_list(rlist):
    """Test RecipeList class, checks if it calls and reads the json appropriately

    Args:
        rlist (RecipeList): A RecipeList instance
    """
    assert len(rlist.recipes) == 6
    assert type(rlist.recipes) == list
    assert isinstance(rlist.recipes[0], Recipe) == True


def test_not_recipe_list():
    """
    Checks for errors if no datastore is given
    """
    with pytest.raises(FileNotFoundError):
        not_rlist = RecipeList([Path("./unit_tests/not_example.json")])


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
    assert len([random_recipe]) == 1
    assert isinstance(random_recipe, Recipe) == True


#     # get a list of recipes back, based on ingredients
#     # capitalization shouldn't matter on the user's end
#     ingr_recipes = rlist.by_ingredients(INGREDIENTS)
#     for i in ingr_recipes[0]['ingredients']:
#         assert i in INGREDIENTS
