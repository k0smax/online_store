import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product_tomato():
    return Product("Помидор", "Красный помидор", 345.99, 25)


@pytest.fixture()
def product_cucumber():
    return Product("Огурец", "Огурец тепличный", 200.99, 100)


@pytest.fixture()
def product_pepper():
    return Product("Перец", "Перец красный", 150.99, 15)


@pytest.fixture()
def product_vegetables(product_tomato, product_cucumber, product_pepper):
    return Category("Овощи", "Овощи", [product_tomato, product_cucumber, product_pepper])
