from __future__ import annotations
class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other: Box3D):
        if type(other) != Box3D:
            raise ArithmeticError('add only Box3D')
        return Box3D(self.width+other.width, self.height + other.height\
                     ,self.depth+ other.depth)

    def __mul__(self, other):
        if type(other) != int:
            raise ArithmeticError()
        return Box3D(self.width* other, self.height*other, self.depth*other)

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other:Box3D):
        if type(other) != Box3D:
            raise ArithmeticError()
        return Box3D(self.width - other.width, self.height - other.height\
                     , self.depth - other.depth)
    def __floordiv__(self, other):
        if type(other) != int:
            raise ArithmeticError()
        return Box3D(self.width// other, self.height//other, self.depth//other)

    def __mod__(self, other):
        if type(other) != int:
            raise ArithmeticError()
        return Box3D(self.width % other, self.height % other, self.depth % other)
