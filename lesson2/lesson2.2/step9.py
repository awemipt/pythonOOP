class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.lines = list(args)

    def get_path(self):
        print(self.lines)

    def get_length(self):
        px, py = 0, 0
        l = 0
        for line in self.lines:
            l += ((line.x- px) **2 + (line.y- py) **2)**.5
            px, py = line.x, line.y
        return l

    def add_line(self, line):
        self.lines.append(line)

p = PathLines(LineTo(40, 30))
dist = p.get_length()
print(dist)