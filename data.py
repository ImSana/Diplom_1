from dataclasses import dataclass
from ingredient_types import INGREDIENT_TYPE_SAUCE


@dataclass
class Data:
    BUN_NAME: str = 'Булка'
    BUN_PRICE: float = 11.1
    INGREDIENT_NAME: str = 'Соус Spicy-X'
    INGREDIENT_TYPE: str = INGREDIENT_TYPE_SAUCE
    INGREDIENT_PRICE: float = 5.5
