class LengthValidator:
    def __init__(self, min_length, max_length):
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, *args, **kwargs):
        if len(args) > 1:
            raise AttributeError()
        return self.__min_length <= len(args[0]) <= self.__max_length

class CharsValidator:
    def __init__(self, chars):
        self.__chars = set(chars)

    def __call__(self, *args, **kwargs):
        if len(args) > 1:
            raise AttributeError()
        return not set(args[0]) - self.__chars

ch = CharsValidator('abc')
print(ch('aabv'))
print(ch('aab'))