class Vector:
    def __init__(self, *args):
        self.coords = list(args)
        self.dim = len(args)

    def __add__(self, other):
        if self.dim != other.dim:
            raise TypeError('размерности векторов не совпадают')
        return Vector(*[x + y for x, y in zip(self.coords, other.coords)])

    def __sub__(self, other):
        if self.dim != other.dim:
            raise TypeError('размерности векторов не совпадают')
        return Vector(*[x - y for x, y in zip(self.coords, other.coords)])

    def get_coords(self):
        return tuple(self.coords)


class VectorInt(Vector):
    def __init__(self, *args):
        super().__init__(*args)
        if any([type(x) != int for x in self.coords]):
            raise ValueError('координаты должны быть целыми числами')

    def __add__(self, other):
        if self.dim != other.dim:
            raise TypeError('размерности векторов не совпадают')
        if (type(other) == VectorInt):
            return VectorInt(*[x + y for x, y in zip(self.coords, other.coords)])
        else:
            return Vector(*[x + y for x, y in zip(self.coords, other.coords)])

    def __sub__(self, other):
        if self.dim != other.dim:
            raise TypeError('размерности векторов не совпадают')
        if type(other) == VectorInt:
            return VectorInt(*[x - y for x, y in zip(self.coords, other.coords)])
        else:
            return Vector(*[x - y for x, y in zip(self.coords, other.coords)])


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
v = v1 - v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
print(v.get_coords())
