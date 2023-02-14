class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __bool__(self):
        return 'x1' in self.__dict__ and 'x2' in self.__dict__ \
               and 'y1' in self.__dict__ and 'y2' in self.__dict__

    def get_coords(self):
        if self:
            return self.x1, self.y1, self.x2, self.y2
        else:
            raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(1, 2, 3, 4)]
for el in lst_geom:
    if el:
        el.get_coords()
