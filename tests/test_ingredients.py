import random

from praktikum_files.ingredient import Ingredient
from unittest.mock import Mock
import pytest


class TestIngredientsMocked:
    mock_available_ingredients = Mock()
    mock_available_ingredients.return_value = [
        Ingredient('INGREDIENT_TYPE_SAUCE', 'invisible_sauce', 500),
        Ingredient('INGREDIENT_TYPE_SAUCE', 'million scoville space pepper ketchup', 770),
        Ingredient('INGREDIENT_TYPE_SAUCE', 'non-spicy extra smooth shiny sauce', 2),
        Ingredient('INGREDIENT_TYPE_SAUCE', 'spice duck sauce', 14),
        Ingredient('INGREDIENT_TYPE_FILLING', 'unicorn meat', 100),
        Ingredient('INGREDIENT_TYPE_FILLING', 'mermaid lunges', 350)
    ]
    def test_can_make_ingredient(self):
        ingredient = random.choice(self.mock_available_ingredients())
        name = ingredient.name
        price = ingredient.price
        ingredient_type = ingredient.type
        factual_name = ingredient.get_name()
        factual_price = ingredient.get_price()
        factual_type = ingredient.get_type()
        assert name == factual_name and price == factual_price and ingredient_type == factual_type