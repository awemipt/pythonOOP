class PointTrack:
    def __init__(self, x, y):
        if any([type(x) not in (float, int), type(y) not in (float, int), ]):
            raise TypeError('координаты должны быть числами')
        self.x = x
        self.y = y

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


class Track:
    def __init__(self, *args):
        if type(args[0]) == PointTrack:
            self.__points = list(args)
        else:
            self.__points = [PointTrack(args[0], args[1])]

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points = [pt] + self.__points

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


tr = Track(0,0)
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)