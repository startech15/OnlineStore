import datetime

class Cart:
    __last_id = 0
    __dict = dict()

    def __init__(self, id, created, ):
        def __init__(self, title, price):
            self.title = title  # корзин м.б. несколько, поэтому название "Корзина {id}"
            self.price = price  # общая стоимость сложенных в корзину товаров в настоящий момент, при передаче в заказ может измениться
            Cart.__last_id += 1
            self.id = Cart.__last_id
            self.created = datetime.datetime.now()
            self.updated = None
            Cart.__dict.update(self)

        @property
        def price(self):
            return self.__price