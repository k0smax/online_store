class ZeroQuantity(Exception):

    def __init__(self):
        self.message = "Вы пытаетесь добавить товар с нулевым количеством!"

    def __str__(self):
        return self.message
