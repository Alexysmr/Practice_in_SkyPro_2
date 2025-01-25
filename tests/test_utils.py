
from src.utils import read_json, make_from_json

path = "data/products.json"


def test_read_json():
    assert read_json(path) == [{
                                   'description': 'Смартфоны, как средство не только коммуникации, но и получение '
                                                  'дополнительных функций для удобства жизни',
                                   'name': 'Смартфоны', 'products': [
            {'description': '256GB, Серый цвет, 200MP камера', 'name': 'Samsung Galaxy C23 Ultra', 'price': 180000.0,
             'quantity': 5},
            {'description': '512GB, Gray space', 'name': 'Iphone 15', 'price': 210000.0, 'quantity': 8},
            {'description': '1024GB, Синий', 'name': 'Xiaomi Redmi Note 11', 'price': 31000.0, 'quantity': 14}]}, {
                                   'description': 'Современный телевизор, который позволяет наслаждаться просмотром, '
                                                  'станет вашим другом и помощником',
                                   'name': 'Телевизоры', 'products': [
            {'description': 'Фоновая подсветка', 'name': '55" QLED 4K', 'price': 123000.0, 'quantity': 7}]}]


def test_make_from_json():
    list_products, list_object_products, list_object_categorys = make_from_json(path)
    assert type(list_products) is list
    assert len(list_object_products) == 4
    assert len(list_object_categorys) == 2
