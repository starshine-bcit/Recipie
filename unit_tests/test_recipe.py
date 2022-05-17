import pytest
from modules.recipe import Recipe


ID = "1"
NAME = "Recipe name"
INGREDIENTS = ["apple", "orange", "pain"]
INSTRUCTIONS = "These are cooking instructions"


@pytest.fixture
def rcp():
    """
    Creates a Recipe instance, has a name, ingredients, and instructions

    Returns:
        obj: Recipe instance
    """
    recipe = Recipe(ID, NAME, INGREDIENTS, INSTRUCTIONS)
    return recipe


def test_recipe(rcp):
    """
    Tests the Recipe class and ensures it has 3 attributes: name(str), ingredients(list), instructions(str)

    Args:
        rcp (obj): Recipe instance
    """
    assert rcp.name == "Recipe name"
    assert isinstance(rcp.ingredients, list) == True
    assert rcp.instructions == "These are cooking instructions"


def test_recipe_errors():
    """
    Checks the Recipe class for errors, ensures that name is a string, ingredients is a list, and instructions is a string
    """

    with pytest.raises(TypeError):
        recipe = Recipe(ID, 12345, INGREDIENTS, INSTRUCTIONS)
    with pytest.raises(TypeError):
        recipe = Recipe(ID, NAME, "not a list", INSTRUCTIONS)
    with pytest.raises(TypeError):
        recipe = Recipe(ID, NAME, INGREDIENTS, ("not instructions", 1234))


def test_recipe_methods(rcp):
    """
    Checks the Recipe class methods
    to_dict - Ensure that it properly translates the class's attributes into dictionary form
    ingredients_to_str - turns a list into a str with newlines for each item

    Args:
        rcp (obj): Recipe instance
    """
    assert rcp.to_dict() == {
        "id": ID,
        "name": NAME,
        "ingredients": INGREDIENTS,
        "instructions": INSTRUCTIONS,
    }

    # Tests the ingredients to str method
    assert rcp.ingredients_as_str() == "apple\norange\npain"
