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
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """
        Метод для добавления товаров
        :param product: товар
        :return: None
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """ Геттер для вывода списка товаров в виде строк """
        list_product = []
        for product in self.__products:
            list_product.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")

        return "\n".join(list_product)
