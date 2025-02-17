import unittest
from unittest.mock import patch

from src.class_product import Product


def test_product_init(device1):
    assert (device1.name, device1.description, device1.price, device1.quantity) == (
        "Realme 13+",
        "256GB, Розовый цвет, 46MP камера",
        16000.0,
        10,
    )


def test_newproduct_price(monkeypatch):
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    with unittest.mock.patch("builtins.input", side_effect=["y"]):
        new_product.price = 800
        assert new_product.price == 800
