from src.product import Product


class Order:
    """Класс, который описывает заказ"""

    product: Product
    quantity: int

    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity

    @property
    def total_cost(self) -> float:
        """Свойство, которое возвращает общую стоимость купленного товара"""
        return round(self.product.price * self.quantity, 2)
