from src.category import Category
from src.product import Product


def test_category_init(product_vegetables, product_tomato, product_cucumber, product_pepper):
    """ Тест для проверки корректности инициализации объектов класса Category """
    assert product_vegetables.name == "Овощи"
    assert product_vegetables.description == "Овощи"
    assert product_vegetables.products == [product_tomato, product_cucumber, product_pepper]


def test_category_and_product_count():
    """ Тест для проверки правильного подсчета количества продуктов и категорий """
    assert Category.category_count == 1
    assert Category.product_count == 3
    prod_1 = Product("Apple iPhone 15", "512/32, синий", 120000, 3)
    prod_2 = Product("Samsung Galaxy S20", "256/16, серый", 85000, 5)
    cat_1 = Category("Смартфоны", "Премиальные смартфоны", [prod_1, prod_2])
    assert Category.category_count == 2
    assert Category.product_count == 5
