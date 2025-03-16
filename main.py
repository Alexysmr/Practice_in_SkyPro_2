from src.class_category import Category
from src.products import LawnGrass, Smartphone

if __name__ == "__main__":
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.__class__.__name__, ":", smartphone1.name, end=", ")
    print(smartphone1.description, end=", ")
    print(smartphone1.price, end=", ")
    print(smartphone1.quantity, end=", ")
    print(smartphone1.efficiency, end=", ")
    print(smartphone1.model, end=", ")
    print(smartphone1.memory, end=", ")
    print(smartphone1.color)

    print(smartphone2.__class__.__name__, ":", smartphone2.name, end=", ")
    print(smartphone2.description, end=", ")
    print(smartphone2.price, end=", ")
    print(smartphone2.quantity, end=", ")
    print(smartphone2.efficiency, end=", ")
    print(smartphone2.model, end=", ")
    print(smartphone2.memory, end=", ")
    print(smartphone2.color)

    print(smartphone3.__class__.__name__, ":", smartphone3.name, end=", ")
    print(smartphone3.description, end=", ")
    print(smartphone3.price, end=", ")
    print(smartphone3.quantity, end=", ")
    print(smartphone3.efficiency, end=", ")
    print(smartphone3.model, end=", ")
    print(smartphone3.memory, end=", ")
    print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.__class__.__name__, ":", grass1.name, end=", ")
    print(grass1.description, end=", ")
    print(grass1.price, end=", ")
    print(grass1.quantity, end=", ")
    print(grass1.country, end=", ")
    print(grass1.germination_period, end=", ")
    print(grass1.color)

    print(grass2.__class__.__name__, ":", grass2.name, end=", ")
    print(grass2.description, end=", ")
    print(grass2.price, end=", ")
    print(grass2.quantity, end=", ")
    print(grass2.country, end=", ")
    print(grass2.germination_period, end=", ")
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print("Smartphone sum = ", smartphone_sum)

    grass_sum = grass1 + grass2
    print("Grass sum = ", grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
