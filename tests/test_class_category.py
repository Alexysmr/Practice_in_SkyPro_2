from src.class_category import CategorysIteration


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

    assert "Realme 12, 14000.0 руб. Остаток: 7 шт." in CategorysIteration(product_category1).product

    product_category1.add_product(device3())
    assert str(product_category1) == "Смартфоны, количество продуктов: 19 шт."
