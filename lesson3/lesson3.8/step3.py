class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.lines = []

    def add_point(self, x, y, speed):
        self.lines.append([(x, y), speed])

    def __check_indx(self, indx):
        if indx < 0 or indx >= len(self.lines):
            raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        self.__check_indx(key)
        self.lines[key][1] = value

    def __getitem__(self, item):
        self.__check_indx(item)
        return self.lines[item]
