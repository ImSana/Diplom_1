from ingredient_types import INGREDIENT_TYPE_SAUCE
from ingredient import Ingredient


class TestIngredient:
    def test_get_return_price(self):
        add_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 123.0)
        assert add_ingredient.get_price() == 123.0

    def test_get_return_name(self):
        add_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 123.0)
        assert add_ingredient.get_name() == 'Соус Spicy-X'

    def test_get_return_type(self):
        add_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 123.0)
        assert add_ingredient.get_type() == INGREDIENT_TYPE_SAUCE