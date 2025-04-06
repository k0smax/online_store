import json
import os
from typing import Any, Dict

from src.category import Category
from src.product import Product


def reader_json(path_to_file: str) -> Dict[str, Any]:
    """
    Функция подгружает данные из json-файла
    :param path_to_file: относительный путь до файла
    :return: словарь с данными
    """
    absolut_path = os.path.abspath(path_to_file)
    with open(absolut_path, "r", encoding="utf-8") as file:
        data: Dict[str, Any] = json.load(file)
    return data


def create_products_and_category(category_data: dict) -> list:
    """
    Функция создает объекты классов Product и Category из словаря
    :param category_data: словарь с данными
    :return: список экземпляров класса Category
    """
    category_list = []
    for category in category_data:
        product_list = []
        for product in category.get("products"):
            # product_name = product.get("name")
            # product_description = product.get("description")
            # product_price = product.get("price")
            # product_quantity = product.get("quantity")
            # product_list.append(Product(
            #     name=product_name,
            #     description=product_description,
            #     price=product_price,
            #     quantity=product_quantity
            # ))
            product_list.append(Product(**product))
        category["products"] = product_list
        category_list.append(Category(**category))
        # category_name = category.get("name")
        # category_description = category.get("description")
        # category_list.append(Category(
        #     name=category_name,
        #     description=category_description,
        #     products=product_list
        # ))

    return category_list


# if __name__ == "__main__":
#     data = reader_json("../data/products.json")
#     category_list = create_products_and_category(data)
#     for category in category_list:
#         print(category.name)
#         print(category.description)
#         for product in category.products:
#             print(product.name)
#             print(product.description)
#             print(product.price)
#             print(product.quantity)
#
#     print(Category.category_count)
#     print(Category.product_count)
