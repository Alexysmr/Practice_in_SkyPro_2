from abc import ABC, abstractmethod

from src.class_product import Product
from src.exceptions import ZeroQuantityException


class BaseCategory(ABC):
    """Базовый класс для класса Category"""

    @abstractmethod
    def __init__(self):
        pass


class Category(BaseCategory):
    """Класс описания категорий товаров"""

    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1
        self.add_product(products)
        Order(self.name, products)

    def __str__(self):
        self.all_quantity = 0
        for i in self.__products:
            self.all_quantity += i.quantity
        return f"{self.name}, количество продуктов: {self.all_quantity} шт."

    def add_product(self, products: list) -> None:
        """Добавление товара с проверками и обработкой исключений"""
        try:
            if len(products) == 0:
                raise ZeroQuantityException("Товар не добавлен: количество = 0")
            for product in products:
                if not isinstance(product, Product):
                    raise TypeError("Можно добавлять только объекты Product")
                self.__products.append(product)
                Category.product_count += 1
                print(f"Товар '{product.name}' успешно добавлен в категорию '{self.name}'")
        except TypeError as err:
            print(err)
        except ZeroQuantityException as err:
            print(err)
        finally:
            print("Обработка запроса на добавление товара завершена")

    @property
    def products(self) -> list[str]:
        list_products = []
        for i in self.__products:
            list_products.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.")
        return list_products

    def __call__(self, *args, **kwargs) -> list[Product]:
        return self.__products

    def middle_price(self):
        """Возвращает среднюю цену товаров в категории. Если товаров нет, возвращает 0."""
        try:
            total_price = sum(product.price * product.quantity for product in self.__products)
            total_quantity = sum(product.quantity for product in self.__products)
            return round(total_price / total_quantity, 2)
        except ZeroDivisionError:
            return 0


class CategorysIterator:
    """Класс итерации продуктов в экземпляре класса Category"""

    def __init__(self, category):
        self.category = category
        self.product = category.products

    def __iter__(self):
        return iter(self.category.products)

    def __next__(self):
        for i in self.product:
            return i


class Order(Category):
    """Класс вывода информации о покупках"""

    def __init__(self, name: str, products: list[Product]) -> None:
        for i in products:
            print(f"Заказ: {name} - {i.name}; Кол-во: {i.quantity}; Итоговая стоимость: {i.quantity * i.price}")
