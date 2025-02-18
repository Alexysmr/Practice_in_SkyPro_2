class Product:
    """Класс описания товаров"""

    name: str
    description: str
    price: float
    quantity: int
    list_of_products: list[any]
    list_of_products = []

    def __init__(self, name, description, price, quantity):
        new_list = Product.accounting_for_instances([name, description, price, quantity])
        self.name = new_list[0]
        self.description = new_list[1]
        self.__price = new_list[2]
        self.quantity = new_list[3]

    @staticmethod
    def accounting_for_instances(new_list: list) -> list:
        if not Product.list_of_products:
            Product.list_of_products.append(new_list)
        else:
            n = 0
            for i in Product.list_of_products:
                if i[0] == new_list[0]:
                    n += 1
                    i[3] = i[3] + new_list[3]
                    if new_list[2] > i[2]:
                        i[2] = new_list[2]
                    new_list = i
            if n == 0:
                Product.list_of_products.append(new_list)
        return new_list

    @classmethod
    def new_product(cls, dict_product):
        cls.name = dict_product["name"]
        cls.description = dict_product["description"]
        cls.__price = dict_product["price"]
        cls.quantity = dict_product["quantity"]
        return Product(cls.name, cls.description, cls.__price, cls.quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirmation = input(
                f"Предлагаемая новая цена {new_price} ниже текущей {self.price}. Для подтверждения "
                f'установки новой цены введите "y", иное - отмена: -> '
            )
            if confirmation == "y":
                self.__price = new_price
