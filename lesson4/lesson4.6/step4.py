class Digit:
    def __init__(self, value):
        if type(value) not in (float, int):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class Integer(Digit):
    def __init__(self, value):
        if type(value) is not int:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Float(Digit):
    def __init__(self, value):
        if type(value) is not float:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Positive(Digit):
    def __init__(self, value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Negative(Digit):
    def __init__(self, value):
        if value > 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    @staticmethod
    def is_prime(value):
        if value == 2:
            return True
        for i in range(2, int(value ** .5) + 1, 2):
            if value % i == 0:
                return False
        return True

    def __init__(self, value):
        if not self.is_prime(value):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class FloatPositive(Float, Positive):
    def __init__(self, value):
        super(FloatPositive, self).__init__(value)




digits = [PrimeNumber(2), PrimeNumber(3), PrimeNumber(5),
          FloatPositive(1.), FloatPositive(1.23), FloatPositive(23.),
          FloatPositive(1.2), FloatPositive(22.2)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
print(lst_positive, lst_float)
