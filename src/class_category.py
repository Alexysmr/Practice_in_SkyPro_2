class Category:
    """Класс описания категорий товаров"""

    name: str
    description: str
    products: list[any]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        list_products = []
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1
        for i in self.__products:
            list_products.append(f"{i.name}, {i.price} руб. Остаток {i.quantity} шт.")
        self.__products = list_products

    def add_product(self, products):
        self.products.append(f"{products.name}, {products.price} руб. Остаток {products.quantity} шт.")
        Category.product_count += len([products])

    @property
    def products(self):
        return self.__products
