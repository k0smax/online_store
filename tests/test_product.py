from unittest.mock import patch

import pytest

from src.product import Product


@pytest.mark.parametrize(
    "product, expected_name, expected_description, expected_price, expected_quantity", [
        ("product_tomato", "Помидор", "Красный помидор", 345.99, 25),
        ("product_cucumber", "Огурец", "Огурец тепличный", 200.99, 100),
        ("product_pepper", "Перец", "Перец красный", 150.99, 15)
    ]
)
def test_init(product, expected_name, expected_description, expected_price, expected_quantity, request):
    """ Тест, для проверки корректности инициализации объектов класса Product и геттера price """
    product = request.getfixturevalue(product)
    assert product.name == expected_name
    assert product.description == expected_description
    assert product.price == expected_price
    assert product.quantity == expected_quantity


@pytest.mark.parametrize(
    "price, cap_out, return_value, finish_price", [
        (0, "Цена не должна быть нулевая или отрицательная\n", None, 230),
        (-100, "Цена не должна быть нулевая или отрицательная\n", None, 230),
        (200, "Вы действительно хотите понизить цену?\n", "y", 200),
        (200, "Вы действительно хотите понизить цену?\n", "n", 230),
        (240, "", None, 240),
    ]
)
def test_products_setter_price(product_apple, price, cap_out, return_value, finish_price, capsys):
    """Тест для проверки сеттера price"""
    product_1 = product_apple
    with patch("builtins.input", return_value=return_value):
        product_1.price = price
        captured = capsys.readouterr()
        assert captured.out == cap_out
        assert product_1.price == finish_price


@pytest.mark.parametrize(
    "name, description, price, quantity, exp_name, exp_price, exp_quantity, product_list", [
        ("Груша", "Желтая, мягкая", 180, 90, "Груша", 180, 90, []),
        ("Яблоко", "Желтое, мягкое", 260, 60, "Яблоко", 260, 160,
         [Product("Яблоко", "Желтое, мягкое", 250, 100)]),
    ]
)
def test_products_new_product(name, description, price, quantity, exp_name, exp_price, exp_quantity, product_list):
    """Тест для проверки класс-метода new_product"""
    product_list = product_list
    product_dict = {
        "name": name,
        "description": description,
        "price": price,
        "quantity": quantity
    }
    product_2 = Product.new_product(product_dict, product_list)
    assert product_2.name == exp_name
    assert product_2.description == description
    assert product_2.price == exp_price
    assert product_2.quantity == exp_quantity


def test_product_str(product_apple):
    """Тест для проверки работоспособности магического метода __str__"""
    assert str(product_apple) == "Яблоко Голландское, 230 руб. Остаток: 100 шт."


def test_product_add(product_tomato, product_cucumber):
    """Тест для проверки работоспособности магического метода __add__"""
    assert product_tomato + product_cucumber == 28748.75


def test_product_add_error(iphone_15, shady_lawn):
    """Тест для проверки исключения при сложении объектов разных классов"""
    with pytest.raises(TypeError):
        price = iphone_15 + shady_lawn
