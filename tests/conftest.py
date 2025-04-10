import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def product_tomato():
    return Product("Помидор", "Красный помидор", 345.99, 25)


@pytest.fixture
def product_cucumber():
    return Product("Огурец", "Огурец тепличный", 200.99, 100)


@pytest.fixture
def product_pepper():
    return Product("Перец", "Перец красный", 150.99, 15)


@pytest.fixture
def product_vegetables(product_tomato, product_cucumber, product_pepper):
    return Category("Овощи", "Овощи", [product_tomato, product_cucumber, product_pepper])

@pytest.fixture
def product_apple():
    return Product("Яблоко Голландское", "Красное, сочное", 230, 100)

@pytest.fixture
def iphone_15():
    return Smartphone(
        name="iPhone 15 Pro",
        description="Флагманский смартфон от Apple с процессором A17 Pro и камерой 48 МП",
        price=999.99,
        quantity=10,
        efficiency=90.6,
        model="iPhone 15 Pro",
        memory=8,
        color="Титановый серый"
    )

@pytest.fixture
def shady_lawn():
    return LawnGrass(
        name="ТеньMaster для затенённых участков",
        description="Специальная смесь для мест с недостатком солнечного света",
        price=32.5,
        quantity=30,
        country="Россия",
        germination_period="21-28 дней",
        color="Тёмно-зелёный"
    )
