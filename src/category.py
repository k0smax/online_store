from abc import ABC, abstractmethod
from typing import Optional, Self

from src.exceptions import ZeroQuantity
from src.product import Product


class CategoryOrderContainer(ABC):
    """ Абстрактный класс для классов Category и Order """

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def add_product(self, *args, **kwargs) -> None:
        pass


class Category(CategoryOrderContainer):
    """
    Класс, который описывает категории товаров
    """

    name: str  # Наименование категории
    description: str  # Описание категории
    __products: list[Product]  # Список продуктов в данной категорий

    category_count = 0  # Количество категорий
    product_count = 0  # Количество товаров в целом

    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None) -> None:
        self.name = name
        self.description = description
        if products:
            self.__products = products
            Category.product_count += len(products)
        else:
            self.__products = []
        Category.category_count += 1

    def __str__(self) -> str:
        quantity_products = 0
        for product in self.__products:
            quantity_products += product.quantity
        return f"{self.name}, количество продуктов: {quantity_products} шт."

    def add_product(self, product: Product) -> None:
        """
        Метод для добавления товаров
        :param product: товар
        :return: None
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        try:
            if product.quantity <= 0:
                raise ZeroQuantity
            self.__products.append(product)
            Category.product_count += 1
            print("Товар добавлен!")
        except ZeroQuantity as exc_info:
            print(exc_info)
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self) -> str:
        """Геттер для вывода списка товаров в виде строк"""
        list_product = []
        for product in self.__products:
            list_product.append(str(product))

        return "\n".join(list_product)

    def middle_price(self):
        """Метод для расчета средней цены товаров в категории"""
        list_price = [product.price for product in self.__products]
        try:
            return round(sum(list_price) / len(list_price), 2)
        except ZeroDivisionError:
            return 0


class IterCategory:

    def __init__(self, category_obj: Category) -> None:
        self.category_obj = category_obj
        self.index = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> str:
        if self.index < len(self.category_obj.products.split("\n")):
            product = self.category_obj.products.split("\n")[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
