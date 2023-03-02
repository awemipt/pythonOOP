class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        name = list(kwargs)[0] if kwargs else None
        if name:
            setattr(self, name, kwargs[name])

    def __str__(self):
        if not self.__dict__:
            return "Первичный ключ должен быть целым неотрицательным числом"
        name = list(self.__dict__)[0]
        if getattr(self, name) is not int or getattr(self, name) < 0:
            return f"Значение первичного ключа {name} = {getattr(self, name)} недопустимо"
e2 = PrimaryKeyError(id=-10.5)  # Значение первичного ключа id = abc недопустимо

print(e2)