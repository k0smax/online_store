from abc import ABC, abstractmethod
from typing import Any, Optional, Self

from src.mixin_info_class import MixinInfoClass


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для товаров.
    Определяет обязательные атрибуты и методы, которые должны быть реализованы в дочерних классах.
    """
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод для строкового представления продукта"""
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        """Абстрактный метод для сложения продуктов (по стоимости с учетом количества)"""
        pass

    # def __repr__(self):
    #     return (f"{self.__class__.__name__}('{self.name}', '{self.description}',"
    #             f" '{self.price}', '{self.quantity}')")

    @property
    @abstractmethod
    def price(self) -> float:
        """Геттер для получения значения цены на товар"""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, info_data: dict, list_products: Optional[list[Self]] = None) -> Self:
        pass


class Product(BaseProduct, MixinInfoClass):
    """
    Класс, который описывает товары
    """
    name: str  # Наименование продукта
    description: str  # Описание продукта
    price: float  # Цена продукта
    quantity: int  # Количество штук продукта

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для property
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        if not type(self) is type(other):
            raise TypeError("Можно складывать только продукты только одного класса!")
        return round(self.price * self.quantity + other.price * other.quantity, 2)

    @property
    def price(self) -> float:
        """Геттер для получения значения цены на товар"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер для изменения цены на товар
        :param new_price: новая цена на товар
        :return: None
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            print("Вы действительно хотите понизить цену?")
            user_input = input("Введите y, если да. Введите n для отмены: ")
            if user_input.lower() != "y":
                self.__price = self.__price
            else:
                self.__price = new_price
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, info_data: dict, list_products: Optional[list[Self]] = None) -> Self:
        """
        Класс-метод для добавления нового продукта
        :param info_data: информация по новому продукту, представленная словарем с ключами
        "name", "description", "price", "quantity"
        :param list_products: список продуктов с которым сравнивается добавляемый продукт
        :return: экземпляр класса Product (либо новый, либо существующий)
        """
        name = info_data["name"]
        quantity = info_data["quantity"]
        price = info_data["price"]
        # description = info_data["description"]

        if list_products is None:
            list_products = []

        # Проверяем, существует ли похожий продукт в списке продуктов.
        # Если существует - то изменяем его параметры в соответствии с передаваемыми данными
        # Если не существует, то создаем новый продукт
        for product in list_products:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product

        return cls(**info_data)


if __name__ == "__main__":
    tomato = Product("Помидор", "Красный помидор", 345.99, 25)
    cucumber = Product("Огурец", "Огурец тепличный", 200.99, 100)
    # print(tomato)
    # print(type(tomato))
    # print(type(cucumber))
    # print(tomato.__class__)
    # print(cucumber.__class__)
    print(Product.__mro__)
