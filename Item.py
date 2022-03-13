import datetime

class Item:
    __last_id = 0
    # __list = list()
    __dict = dict()

    def __init__(self, title, price):
        self.title = title
        self.price = price
        Item.__last_id += 1
        self.id = Item.__last_id
        self.created = datetime.datetime.now()
        self.updated = None
        # Item.__list.append(self)
        Item.__dict.update(self)

    @property
    def price(self):
        return self.__price

