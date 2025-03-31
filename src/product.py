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
        self.price = price
        self.quantity = quantity
