# 30
# https://app.diagrams.net/?src=about#G143OSHvyPSHf-vfYP4lWS88KTtNqX5lcU

class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Administrator(User):

    def __init__(self, id, name):
        super().__init__(id, name)

    def cat_edit(self):  # метод для редактирования каталога
        pass

    def price_edit(self):  # метод для редактирования прайслиста
        pass
