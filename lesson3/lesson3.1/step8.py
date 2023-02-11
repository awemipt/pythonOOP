class Circle:
    attrs = {'x': (int, float), 'y': (int, float), 'z': (int, float)}

    def __init__(self, x, y, radius):
        self.__x = self.__y = self.__radius = None
        self.x = x
        self.y = y
        self.radius = radius

    def __setattr__(self, key, value):

        if key in ['x', 'y', 'radius']:
            if type(value) in [int, float]:
                if key == 'radius':
                     if value <= 0:
                        return 
            else:
                raise TypeError("Неверный тип присваиваемых данных.")
        super(Circle, self).__setattr__(key, value)
        

    def __getattr__(self, item):
        return False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value


circle = Circle(10.5, 7, 22)
circle.radius = -0  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
circle.x = 2
res = circle.name  # False, т.к. атрибут name не существует
print(circle.__dict__)
