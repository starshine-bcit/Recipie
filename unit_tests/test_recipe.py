import pytest
from modules.recipe import Recipe


ID = 1
NAME = "Recipe name"
DIETS = ['vegetarian', 'vegan']
INGREDIENTS = ["apple", "orange", "pain"]
INSTRUCTIONS = "These are cooking instructions"


@pytest.fixture
def rcp():
    """
    Creates a Recipe instance, has a name, ingredients, and instructions

    Returns:
        obj: Recipe instance
    """
    recipe = Recipe(
        ID, NAME, INGREDIENTS, INSTRUCTIONS, DIETS
    )
    return recipe


def test_recipe(rcp):
    """
    Tests the Recipe class and ensures it has 5 attributes:
        id (int), name(str), diet(list), ingredients(list), instructions(str)

    Args:
        rcp (obj): Recipe instance
    """
    assert rcp.id == 1
    assert rcp.name == "Recipe name"
    assert isinstance(rcp.ingredients, list) == True
    assert rcp.ingredients == ["apple", "orange", "pain"]
    assert isinstance(rcp.diets, list) == True
    assert rcp.diets == ['vegetarian', 'vegan']
    assert rcp.instructions == "These are cooking instructions"


def test_recipe_errors():
    """
    Checks the Recipe class for errors, ensures that id is an integer,
    name is a string, diets is a list, ingredients is a list,
    and instructions is a string.
    """

    with pytest.raises(TypeError):
        recipe = Recipe('a', NAME, INGREDIENTS, INSTRUCTIONS, DIETS)
    with pytest.raises(TypeError):
        recipe = Recipe(1, 12345, INGREDIENTS, INSTRUCTIONS, DIETS)
    with pytest.raises(TypeError):
        recipe = Recipe(1, NAME, "not a list", INGREDIENTS, INSTRUCTIONS, DIETS)
    with pytest.raises(TypeError):
        recipe = Recipe(1, NAME, ['not', 1,'list'], INGREDIENTS, INSTRUCTIONS, DIETS)
    with pytest.raises(TypeError):
        recipe = Recipe(1, NAME, "not a list", INSTRUCTIONS, DIETS)
    with pytest.raises(TypeError):
        recipe = Recipe(1, NAME, ['not', 1,'list'], INSTRUCTIONS, DIETS)
    with pytest.raises(TypeError):
        recipe = Recipe(1, NAME, INGREDIENTS, ("not instructions", 1234), DIETS)

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
        "diets": DIETS
    }

    # Tests the ingredients to str method
    assert rcp.ingredients_as_str() == "apple\norange\npain"
