class Category:
    """Класс описания категорий товаров"""

    name: str
    description: str
    products: list[any]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def __str__(self):
        self.all_quantity = 0
        for i in self.__products:
            self.all_quantity += i.quantity
        return f"{self.name}, количество продуктов: {self.all_quantity} шт."

    def add_product(self, products):
        self.__products.append(products)
        Category.product_count += 1

    @property
    def products(self):
        list_products = []
        for i in self.__products:
            list_products.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.")
        return list_products

    def __call__(self, *args, **kwargs):
        return self.__products


class CategorysIteration:
    """Класс итерации продуктов в экземпляре класса Category"""

    def __init__(self, category):
        self.category = category
        self.product = category.products

    def __iter__(self):
        return self

    def __next__(self):
        for i in self.product:
            return i
