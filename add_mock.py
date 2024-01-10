from unittest.mock import Mock
from data import Data


class Add_Mock:

    @staticmethod
    def mock_ingredient(type=Data.INGREDIENT_TYPE, name=Data.INGREDIENT_NAME, price=Data.INGREDIENT_PRICE):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = type
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        return mock_ingredient

    @staticmethod
    def mock_bun(name=Data.BUN_NAME, price=Data.BUN_PRICE):
        mock_bun = Mock()
        mock_bun.get_name.return_value = name
        mock_bun.get_price.return_value = price
        return mock_bun