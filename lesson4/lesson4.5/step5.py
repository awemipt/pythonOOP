class Validator:
    def __init__(self, data):
        self.data = data

    def is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    def is_valid(self, *args):
        # print(args)
        return not (type(args[0]) is not float or any([args[0] < self._min_value, args[0] > self._max_value]))

    def __call__(self, *args, **kwargs):
        return self.is_valid(*args)


float_validator = FloatValidator(0, 10.5)
res_1 = float_validator(1)  # False (целое число, а не вещественное)
res_2 = float_validator(1.0)  # True
res_3 = float_validator(-1.0)
print(res_1, res_2, res_3)
