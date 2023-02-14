class PolyLine:
    def __init__(self, *args):
        self.coords = list(args)

    def add_coord(self, *coord):
        self.coords.append(coord)

    def remove_coord(self, indx):
        self.coords.pop(indx)

    def get_coords(self):
        return self.coords
