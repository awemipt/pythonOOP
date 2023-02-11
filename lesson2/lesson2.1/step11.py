import random
from string import ascii_letters, digits
class EmailValidator:
    SYMBOLS = ascii_letters + '_' + digits
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        length = random.randint(1, 100)
        email = ''
        for i in range(length):
            email += cls.SYMBOLS[random.randint(0,len(cls.SYMBOLS)-1)]
        return email + '@gmail.com'

    @staticmethod
    def __is_email_str(email):
        if type(email) is str:
            return True
        return False

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        words = email.split('@')
        if len(words) != 2:
            return False
        if len(words[0]) > 100:
            return False
        if len(words[1]) > 50 or '.' not in words[1]:
            return False
        if '..' in words[1] or '..' in words[0]:
            return False
        return True

