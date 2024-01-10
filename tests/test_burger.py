import pytest
from unittest.mock import Mock
from add_mock import Add_Mock


class TestBurger:
    def test_set_buns_one_bun(self, add_burger):
        mock_bun = Add_Mock.mock_bun()
        add_burger.set_buns(mock_bun)
        assert add_burger.bun == mock_bun

    def test_add_ingredient_one_ingredient(self, add_burger):
        mock_ingredient = Add_Mock.mock_ingredient()
        add_burger.add_ingredient(mock_ingredient)
        assert len(add_burger.ingredients) == 1


    def test_remove_ingredients_empty_list_result(self, add_burger):
        mock_ingredient = Mock()
        add_burger.add_ingredient(mock_ingredient)
        add_burger.remove_ingredient(0)
        assert mock_ingredient not in add_burger.ingredients, "Ингридиент не удален и остался в списке ингридиентов"

    def test_move_ingredients_moves_two_ingredients(self, add_burger):
        mock_ingredient_1 = Add_Mock.mock_ingredient()
        mock_ingredient_2 = Add_Mock.mock_ingredient()
        add_burger.add_ingredient(mock_ingredient_1)
        add_burger.add_ingredient(mock_ingredient_2)
        add_burger.move_ingredient(0, 1)
        assert add_burger.ingredients == [mock_ingredient_2, mock_ingredient_1], (
                                         f"Места ингридиентов не соответствуют. Ожидалось: "
                                         f"{[mock_ingredient_2, mock_ingredient_1]}, фактически: "
                                         f"{add_burger.ingredients}")

    @pytest.mark.parametrize('bun_price, ingredient_price, total_price', [(15, 5, 35), (8, 0, 16)])
    def test_get_return_price(self, add_burger, bun_price, ingredient_price, total_price):
        mock_bun = Add_Mock.mock_bun(price=bun_price)
        mock_ingredient_1 = Add_Mock.mock_ingredient(price=ingredient_price)
        add_burger.bun = mock_bun
        add_burger.ingredients = [mock_ingredient_1]
        assert add_burger.get_price() == total_price

    def test_get_return_receipt(self, add_burger):
        mock_bun = Add_Mock.mock_bun()
        mock_ingredient = Add_Mock.mock_ingredient()
        add_burger.bun = mock_bun
        add_burger.ingredients = [mock_ingredient]
        receipt = '\n'.join([f'(==== {mock_bun.get_name.return_value} ====)',
                             f'= {str(mock_ingredient.get_type()).lower()} {mock_ingredient.get_name()} =',
                             f'(==== {add_burger.bun.get_name()} ====)\n',
                             f'Price: {add_burger.get_price()}'])

        assert add_burger.get_receipt() == receipt