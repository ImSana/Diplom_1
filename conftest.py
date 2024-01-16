import pytest
from ingredient_types import INGREDIENT_TYPE_SAUCE
from ingredient import Ingredient
from burger import Burger
from bun import Bun


@pytest.fixture
def add_ingredient():
    new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 5.5)
    return new_ingredient


@pytest.fixture
def add_bun():
    new_bun = Bun('Краторная булка N-200i', 111.1)
    return new_bun


@pytest.fixture
def add_burger():
    new_burger = Burger()
    return new_burger
