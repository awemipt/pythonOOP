from string import ascii_lowercase, digits

rus = ''.join([chr(x) for x in range(ord('а'), ord('я') + 1)])


# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    chars = rus + ascii_lowercase
    CHARS_CORRECT = chars.upper() + chars + digits + ' '

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f'<p class=\'login\'>{self.name}: <input type=\'text\' size={self.size} />'

    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 50 or set(name) - set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")


class PasswordInput:
    chars = rus + ascii_lowercase
    CHARS_CORRECT = chars.upper() + chars + digits + ' '

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f'<p class=\'password\'>{self.name}: <input type=\'text\' size={self.size} />'

    @classmethod
    def check_name(cls, name):
        if len(name) <3 or len(name)>50 or set(name) - set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
