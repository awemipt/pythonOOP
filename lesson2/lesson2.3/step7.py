from typing import Callable


class ValidateString:
    def __init__(self, min_length=3, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        # print(string)
        if not type(string) is str or len(string) > self.max_length or len(string) < self.min_length:
            return False
        return True


class StringValue:
    def __init__(self, validator: ValidateString):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        # print(owner)
        return instance.__dict__[self.name]


class RegisterForm:
    MAX_LENGTH = 50
    MIN_LENGTH = 3
    login = StringValue(ValidateString())
    password = StringValue(ValidateString())
    email = StringValue(ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form> '
              )


a = RegisterForm('acb', '12c', 'adva')
# print(a.__dict__)
a.show()