from typing import Optional, Self, Any


class Product:
    """
    Класс, который описывает товары
    """

    name: str  # Наименование продукта
    description: str  # Описание продукта
    __price: float  # Цена продукта
    quantity: int  # Количество штук продукта

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        if not type(self) is type(other):
            raise TypeError("Можно складывать только продукты только одного класса!")
        return round(self.price * self.quantity + other.__price * other.quantity, 2)

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
    print(tomato)
    print(type(tomato))
    print(type(cucumber))
    print(tomato.__class__)
    print(cucumber.__class__)
