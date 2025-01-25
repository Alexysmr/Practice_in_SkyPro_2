import pytest

from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def device1():
    device = Product("Realme 13+", "256GB, Розовый цвет, 46MP камера", 16000.0, 5)
    return device


@pytest.fixture
def device2():
    device = Product("Realme 12", "128GB, Розовый цвет, 46MP камера", 14000.0, 7)
    return device


@pytest.fixture
def device3():
    device = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    return device


@pytest.fixture
def product_category1(device1, device2):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций "
                    "для удобства жизни",
                    [device1, device2])


@pytest.fixture
def product_category2(device3):
    return Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим "
                         "другом и помощником",
                    [device3])