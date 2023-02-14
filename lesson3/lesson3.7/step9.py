class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __len__(self):
        return len(self.coords)

    def __add__(self, other):
        if type(other) == int:
            ans = [x + other for x in self.coords]
            return Vector(*ans)
        elif type(other) == Vector:
            if len(other) != len(self):
                raise ArithmeticError('размерности векторов не совпадают')
            ans = [x + y for x, y in zip(self.coords, other.coords)]
            return Vector(*ans)

    def __mul__(self, other):
        if type(other) == int:
            ans = [x * other for x in self.coords]
            return Vector(*ans)
        elif type(other) == Vector:
            if len(other) != len(self):
                raise ArithmeticError('размерности векторов не совпадают')
            ans = [x * y for x, y in zip(self.coords, other.coords)]
            return Vector(*ans)

    def __sub__(self, other):
        if type(other) == int:
            ans = [x - other for x in self.coords]
            return Vector(*ans)
        elif type(other) == Vector:
            if len(other) != len(self):
                raise ArithmeticError('размерности векторов не совпадают')
            ans = [x - y for x, y in zip(self.coords, other.coords)]
            return Vector(*ans)

    def __eq__(self, other):
        return all([x == y for x, y in zip(self.coords, other.coords)])
