from typing import Self


class Product:
    """
    Класс, который описывает товары
    """
    name: str  # Наименование продукта
    description: str  # Описание продукта
    price: float  # Цена продукта
    quantity: int  # Количество штук продукта

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """ Геттер для получения значения цены на товар """
        return self.__price

    @price.setter
    def price(self, new_price: int) -> None:
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
    def new_product(cls, info_data: dict, list_products=None) -> Self:
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
        description = info_data["description"]

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

        return cls(name, description, price, quantity)


if __name__ == "__main__":
    pass
    # existing_products = []
    # product1 = Product("Apple", "Apple", 1.5, 10)
    # existing_products.append(product1)
    # product2 = Product("Orange", "Orange", 2.0, 5)
    # existing_products.append(product2)
    # product3 = Product.new_product({"name": "Apple", "description": "Apple", "price": 1.7, "quantity": 20}, existing_products)
    # # existing_products.append(product3)
    #
    # for product in existing_products:
    #     print(product.name, product.price, product.quantity)
