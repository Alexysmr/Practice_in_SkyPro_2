
def test_product_init(device1):
    assert (device1.name, device1.description, device1.price, device1.quantity) == (
    "Realme 13+", "256GB, Розовый цвет, 46MP камера", 16000.0, 5)
