from src.category import Category
from src.product import Product


def test_category_init(product_vegetables, product_tomato, product_cucumber, product_pepper):
    """ Тест для проверки корректности инициализации объектов класса Category """
    assert product_vegetables.name == "Овощи"
    assert product_vegetables.description == "Овощи"
    assert (product_vegetables.products ==
            (f"{product_tomato.name}, {product_tomato.price} руб. Остаток: {product_tomato.quantity} шт.\n"
             f"{product_cucumber.name}, {product_cucumber.price} руб. Остаток: {product_cucumber.quantity} шт.\n"
             f"{product_pepper.name}, {product_pepper.price} руб. Остаток: {product_pepper.quantity} шт."))


def test_category_and_product_count():
    """ Тест для проверки правильного подсчета количества продуктов и категорий """
    assert Category.category_count == 1
    assert Category.product_count == 3
    prod_1 = Product("Apple iPhone 15", "512/32, синий", 120000, 3)
    prod_2 = Product("Samsung Galaxy S20", "256/16, серый", 85000, 5)
    cat_1 = Category("Смартфоны", "Премиальные смартфоны", [prod_1, prod_2])
    assert Category.category_count == 2
    assert Category.product_count == 5


def test_category_add_product(product_apple):
    """ Тест для проверки правильной работы метода add_product и геттера products класса Category """
    product_1 = product_apple
    fruits_category = Category("Фрукты", "Фрукты плодовые", [])
    assert Category.product_count == 5
    fruits_category.add_product(product_1)
    assert Category.product_count == 6
    assert fruits_category.products == "Яблоко Голландское, 230 руб. Остаток: 100 шт."