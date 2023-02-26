from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return f"Базовый класс {self.__class__.__name__}"


class ModelForm(Model):
    __id = 0
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.__class__.__id
        self.__class__.__id += 1

    def get_pk(self):
        return self._id

form = ModelForm("Логин", "Пароль")
form = ModelForm("Логин", "Пароль")
print(form.get_pk())