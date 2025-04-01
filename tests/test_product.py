import pytest


@pytest.mark.parametrize(
    "product, expected_name, expected_description, expected_price, expected_quantity", [
        ("product_tomato", "Помидор", "Красный помидор", 345.99, 25),
        ("product_cucumber", "Огурец", "Огурец тепличный", 200.99, 100),
        ("product_pepper", "Перец", "Перец красный", 150.99, 15)
    ]
)
def test_init(product, expected_name, expected_description, expected_price, expected_quantity, request):
    """ Тест, для проверки корректности инициализации объектов класса Product """
    product = request.getfixturevalue(product)
    assert product.name == expected_name
    assert product.description == expected_description
    assert product.price == expected_price
    assert product.quantity == expected_quantity
