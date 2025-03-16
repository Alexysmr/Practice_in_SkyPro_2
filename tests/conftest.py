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
    device = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    return device


@pytest.fixture
def product_category1(device1, device2):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [device1, device2],
    )


@pytest.fixture
def product_category2(device3):
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [device3],
    )


@pytest.fixture
def smartphone1():
    return {
        "name": "Realme Realme 13+",
        "description": "256GB, Розовый цвет, 46MP камера",
        "price": 16000.0,
        "quantity": 5,
        "efficiency": 98.0,
        "model": "Realme 13+",
        "memory": 256,
        "color": "Розовый",
    }


@pytest.fixture
def smartphone2():
    return {
        "name": "Realme Realme 12",
        "description": "128GB, Серебристый цвет, 48MP камера",
        "price": 14000.0,
        "quantity": 7,
        "efficiency": 89.0,
        "model": "Realme 12",
        "memory": 128,
        "color": "Серебристый",
    }


@pytest.fixture
def lawngrass1():
    return {
        "name": "Трын-трава",
        "description": "Трава волшебная, сказочная",
        "price": 15,
        "quantity": 10,
        "country": "Русь",
        "germination_period": "10 дней",
        "color": "Чистый малахит",
    }
