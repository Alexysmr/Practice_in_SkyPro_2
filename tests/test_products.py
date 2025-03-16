import pytest

from src.products import LawnGrass, Smartphone


def test_smartphone_init(smartphone1):
    device = Smartphone(**smartphone1)
    assert (
        device.name,
        device.description,
        device.price,
        device.quantity,
        device.efficiency,
        device.model,
        device.memory,
        device.color,
    ) == ("Realme Realme 13+", "256GB, Розовый цвет, 46MP камера", 16000.0, 5, 98.0, "Realme 13+", 256, "Розовый")


def test_lawngrass_init(lawngrass1):
    plant = LawnGrass(**lawngrass1)
    assert (
        plant.name,
        plant.description,
        plant.price,
        plant.quantity,
        plant.country,
        plant.germination_period,
        plant.color,
    ) == ("Трын-трава", "Трава волшебная, сказочная", 15, 10, "Русь", "10 дней", "Чистый малахит")


def test_smartphone_sum(smartphone1, smartphone2):
    assert Smartphone(**smartphone1) + Smartphone(**smartphone2) == 258000.0


def test_wrong_sum_smartphone_and_lawngrass(smartphone1, lawngrass1):
    with pytest.raises(TypeError):
        Smartphone(**smartphone1) + LawnGrass(**lawngrass1)
