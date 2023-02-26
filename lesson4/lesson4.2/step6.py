class Tuple(tuple):
    def __add__(self, other):
        return Tuple(super().__add__(tuple(other)))

print(type(Tuple((1,2,3))+[1,3]))
