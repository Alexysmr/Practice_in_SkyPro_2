from src.class_category import CategorysIterator


def test_category(product_category1, product_category2, device3):
    assert product_category1.name == "Смартфоны"
    assert product_category1.description == (
        "Смартфоны, как средство не только коммуникации, но и получения " "дополнительных функций для удобства жизни"
    )
    assert len(product_category1.products) == 2
    assert product_category2.name == "Телевизоры"
    assert product_category2.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником"
    )
    assert len(product_category2.products) == 1
    assert product_category2.category_count == 2
    assert product_category2.product_count == 3

    assert "Realme 12, 14000.0 руб. Остаток: 7 шт." in CategorysIterator(product_category1).product

    product_category1.add_product(device3())
    assert str(product_category1) == "Смартфоны, количество продуктов: 19 шт."


def test_middle_price(product_category1, empty_product_category):
    assert product_category1.middle_price() == round((16000 * 5 + 14000 * 7) / (5 + 7), 2)
    assert empty_product_category.middle_price() == 0


def test_category_iterator(product_category1):
    iterator = CategorysIterator(product_category1)
    products_list = list(iterator)
    assert len(products_list) == len(product_category1.products)
