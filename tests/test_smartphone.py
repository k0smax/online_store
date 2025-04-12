

def test_init_smartphone(iphone_15):
    """
    Тест, проверяющий правильную инициализацию экземпляра класса Smartphone
    Также проверяет правильную работу методов родительского класса
    """
    assert iphone_15.name == "iPhone 15 Pro"
    assert str(iphone_15) == "iPhone 15 Pro, 999.99 руб. Остаток: 10 шт."
    assert iphone_15.price == 999.99
