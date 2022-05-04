import pytest
from unittest.mock import mock_open, patch
from modules.recipe import Recipe
from modules.recipelist import RecipeList


RECIPE_JSON = {
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
}


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=RECIPE_JSON)
def rlist(mock_file):
    recipelist = RecipeList()
    return recipelist


def test_recipe_list(rlist):
    """Test RecipeList class, checks if 

    Args:
        mock_file (_type_): _description_
    """

    # Opens the datastore
    assert rlist.call_count == 1

    # Checks if we're reading the datastore
    assert rlist.call_args[0][0] == "r"

    assert len(rlist.recipe_list) == 3
    assert (rlist.recipe_list[0], Recipe) == True


def test_not_recipe_list():
    with pytest.raises(FileNotFoundError):
        not_rlist = RecipeList()