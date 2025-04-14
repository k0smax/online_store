from src.product import Product


def test_mixin_info_class(capsys):
    Product("Помидор", "Красный помидор", 345.99, 25)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Помидор', 'Красный помидор', 345.99, 25)"
    