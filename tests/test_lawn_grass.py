

def test_init_smartphone(shady_lawn):
    """
    Тест, проверяющий правильную инициализацию экземпляра класса LawnGrass
    Также проверяет правильную работу методов родительского класса
    """
    assert shady_lawn.name == "ТеньMaster для затенённых участков"
    assert str(shady_lawn) == "ТеньMaster для затенённых участков, 32.5 руб. Остаток: 30 шт."
    assert shady_lawn.price == 32.5
