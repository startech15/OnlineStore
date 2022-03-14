# 30
# https://app.diagrams.net/?src=about#G143OSHvyPSHf-vfYP4lWS88KTtNqX5lcU
# Каталог
# В каталог товары попадают из прайслиста (csv).
# Для неактуальных товаров в прайслисте указывается соответствующий статус (чтобы не удалять, т.к. товары могут снова стать актуальными).
# При переносе товаров в каталог может измениться стоимость.

# Корзина
# Сначала товары попадают в корзину, только потом в заказ (фиксируются по составу, количеству, стоимости).
#

# class User:
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
# class Administrator(User):
#
#     def __init__(self, id, name):
#         super().__init__(id, name)
#
#     def cat_edit(self):  # метод для редактирования каталога
#         pass
#
#     def price_edit(self):  # метод для редактирования прайслиста
#         pass
#
# class Catalog:
#
#     def __init__(self, id, name, price):
#         self.id = id
#         self.name = name
#         self.price = price
#
# class PriceList(Catalog):
#
#     def __init__(self, id, name, price, status):
#         super().__init__(id, name, price)
#         self.status = status
#
# class Cart:
#
#     cart = []
#
#     def addItem(self, item, cart=None): # добавление товаров в корзину
#         self.item = item
#         cart.append(self.item)
#
#     # def removeItem(self):
#     #     try:
#     #         cart.remove(item)
#     #         print('{0} удален.')
#     #     except
#     #         print('{0} не удален.')

# получение каталога
from Catalog import Catalog
catalog = Catalog()
print(catalog.parse())

# создание корзины и добавление в нее товара
from Cart import Cart
cart = Cart()
print('Корзина ' + cart.id, + ':')
print('Список товаров:', sep='\n')
print('На сумму:' + cart.price)

# передача товаров из корзины в заказ
# from Order import Order

