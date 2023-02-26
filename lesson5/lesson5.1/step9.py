class Triange:
    def __init__(self, a, b, c):
        if any(map(lambda x: type(x) not in (float, int) or x < 0,[a, b, c])):
            raise TypeError('стороны треугольника должны быть положительными числами')
        l = list(sorted([a, b, c]))
        if l[0] + l[1] <= l[2]:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')
        self._a = a
        self._b = b
        self._c = c
    def __repr__(self):
        return f'{self._a, self._b, self._c}'

input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []
for x in input_data:
    try:
        lst_tr.append(Triange(*x))
    except:
        pass

print(lst_tr)