from src.product import Product


class Category:
    """
    Класс, который описывает категории товаров
    """
    name: str  # Наименование категории
    description: str  # Описание категории
    products: list[Product]  # Список продуктов в данной категорий

    category_count = 0  # Количество категорий
    product_count = 0  # Количество товаров в целом

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
