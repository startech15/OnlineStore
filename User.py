import datetime

class User:
    __last_id = 0
    __list = list()

    def __init__(self, name, surname, email, phone):
        User.__last_id += 1
        self.id = User.__last_id
        self.name = name  # нужна проверка
        self.surname = surname  # нужна проверка
        self.email = email  # нужна проверка
        self.phone = phone
        self.created = datetime.datetime.now()
        self.updated = None
        self.last_visit = self.created
        self.last_buy = None
        User.__list.append(self)

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone (self, phone):
        set.__phone = phone

    @staticmethod
    def get_user_by_id(id):
        for user in User.__list:
            if user.id == id:
                return user
        raise  ValueError('Пользователь не найден')

    @staticmethod
    def get_user_by_phone(phone):
        for user in User.__list:
            if user.phone == phone:
                return user
        raise  ValueError('Пользователь не найден')

    # заменить эти 2 метода на один - поиск по такому-то полю


    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + self.surname + ' ' + self.phone + ' ' + self.email

