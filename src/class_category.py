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

    def add_product(self, products):
        self.__products.append(products)
        Category.product_count += 1

    @property
    def products(self):
        list_products = []
        for i in self.__products:
            list_products.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.")
        return list_products
