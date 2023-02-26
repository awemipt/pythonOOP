class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        tmp = self.chars
        if not self.chars:
            tmp = string
        # print((set(tmp) & set(string)))
        # print(len(string))
        if any([type(string) is not str, len(string) < self.min_length, len(string) > self.max_length,
                not (set(tmp) & set(string))]):
            raise ValueError('недопустимая строка')
        return string

class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_val = login_validator
        self.pass_val = password_validator
        self._login = None
        self._password = None

    def form(self, request):
        if 'login' not in request or 'password' not in request:
            raise TypeError('в запросе отсутствует логин или пароль')

        self._password = self.pass_val.is_valid(request['password'])
        self._login = self.login_val.is_valid(request['login'])



login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
