from src.product import Product


class Smartphone(Product):
    """Класс, описывающий смартфоны"""

    efficiency: float  # Производительность смартфона
    model: str  # Модель смартфона
    memory: int  # Объем оперативной памяти смартфона
    color: str  # Цвет смартфона

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


# if __name__ == "__main__":
#     iphone_15 = Smartphone(
#         name="iPhone 15 Pro",
#         description="Флагманский смартфон от Apple с процессором A17 Pro и камерой 48 МП",
#         price=999.99,
#         quantity=10,
#         efficiency=90.6,
#         model="iPhone 15 Pro",
#         memory=8,
#         color="Титановый серый"
#     )
#     print(type(iphone_15))
#     print(iphone_15.__class__)
#
#     shady_lawn = LawnGrass(
#         name="ТеньMaster для затенённых участков",
#         description="Специальная смесь для мест с недостатком солнечного света",
#         price=32.5,
#         quantity=30,
#         country="Россия",
#         germination_period="21-28 дней",
#         color="Тёмно-зелёный"
#     )
#     print(type(shady_lawn))
#     print(shady_lawn.__class__)
#     print(shady_lawn + iphone_15)
