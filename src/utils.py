import json
import os

from src.class_category import Category
from src.class_product import Product


def read_json(path: str) -> dict:
    """Функция чтения данных из файла JSON"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def make_from_json(path: str) -> any:
    """Функция создания экземпляров классов Product и Category на основе данных из JSON-файла"""
    data = read_json(path)
    list_products = []
    list_object_categorys = []
    list_object_products = []
    for category in data:
        products = []
        for i in range(len(category["products"])):
            product = category["products"][i]
            intermediate_result = Product(**product)
            products.append(intermediate_result)
            list_products.append(product)
            list_object_products.append(intermediate_result)
        category["products"] = products
        list_object_categorys.append(Category(**category))
    return list_products, list_object_products, list_object_categorys
