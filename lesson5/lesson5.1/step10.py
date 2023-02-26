class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, val, *args, **kwargs):
        if type(val) is not float or val > self.max_value or val < self.min_value:
            raise ValueError('значение не прошло валидацию')

class IntegerValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, val, *args, **kwargs):
        if type(val) is not int or val > self.max_value or val < self.min_value:
            raise ValueError('значение не прошло валидацию')

def is_valid(lst, validators):
    ans = []
    for val in lst:
        for v in validators:
            try:
                v(val)
                ans.append(val)
            except ValueError:
                pass
    return ans

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
print(lst_out)
