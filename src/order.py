from src.category import CategoryOrderContainer
from src.exceptions import ZeroQuantity
from src.product import Product


class Order(CategoryOrderContainer):
    """Класс, который описывает заказ"""

    product: Product
    quantity: int

    def __init__(self) -> None:
        pass

    def add_product(self, product, quantity):
        self.product = product
        try:
            if quantity == 0:
                raise ZeroQuantity
            self.quantity = quantity
            print("Товар добавлен!")
        except ZeroQuantity as exc_info:
            print(exc_info)
        finally:
            print("Обработка добавления товара завершена")


    @property
    def total_cost(self) -> float:
        """Свойство, которое возвращает общую стоимость купленного товара"""
        return round(self.product.price * self.quantity, 2)
