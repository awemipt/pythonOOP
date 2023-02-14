class ListMath:
    def __init__(self, lst=None):
        if lst is None:
            self.lst_math = []
        else:
            self.lst_math = lst
            self.lst_math = [x for x in self.lst_math if type(x) in (float, int)]

    def __add__(self, other):
        if type(other) not in (int, float):
            raise ArithmeticError('операнд должен быть числом')
        ans = [other + x for x in self.lst_math]
        return ListMath(ans)

    def __radd__(self, other):
        return other + self

    def __iadd__(self, other):
        if type(other) not in (int, float):
            raise ArithmeticError('операнд должен быть числом')
        self.lst_math = [x + other for x in self.lst_math]
        return self

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise ArithmeticError('операнд должен быть числом')
        ans = [other * x for x in self.lst_math]
        return ListMath(ans)

    def __rmul__(self, other):
        return  self * other

    def __imul__(self, other):
        if type(other) not in (int, float):
            raise ArithmeticError('операнд должен быть числом')
        self.lst_math = [other * x for x in self.lst_math]
        return self

    def __sub__(self, other):
        if type(other) != int:
            raise ArithmeticError('операнд должен быть числом')
        ans = [x - other  for x in self.lst_math]
        return ListMath(ans)

    def __rsub__(self, other):
        ans = [ other -x for x in self.lst_math]
        return ListMath(ans)

    def __isub__(self, other):
        if type(other) not in (int, float):
            raise ArithmeticError('операнд должен быть числом')
        self.lst_math = [x - other  for x in self.lst_math]
        return self

    def __truediv__(self, other):
        if type(other) != int:
            raise ArithmeticError('операнд должен быть числом')
        ans = [x / other for x in self.lst_math]
        return ListMath(ans)

    def __rtruediv__(self, other):
        ans = [other / x for x in self.lst_math]
        return ListMath(ans)

    def __itruediv__(self, other):
        if type(other) not in (int, float):
            raise ArithmeticError('операнд должен быть числом')
        self.lst_math = [ x/other for x in self.lst_math]
        return self
a =[1, 2, 5, 7.68]
lst1 = ListMath(a)
lst2 = ListMath(a)

lst1 =  76 - lst1
print(lst1.lst_math)