from src.product import Product


class LawnGrass(Product):
    """Класс, описывающий траву-газонную"""

    country: str  # Страна-производитель травы
    germination_period: str  # Срок прорастания травы
    color: str  # Цвет травы

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
