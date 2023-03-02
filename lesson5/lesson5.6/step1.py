import copy
import random
from random import randint


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1] * length

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            if self._tp == 2:
                self._y += go

    def is_collide(self, ship):
        if self._tp == 1:
            coords1 = {(x, y) for x in range(self._x - 1, self._x + self._length + 1) for y in
                       range(self._y - 1, self._y + 2)}
        if self._tp == 2:
            coords1 = {(x, y) for x in range(self._x - 1, self._x + 2) for y in
                       range(self._y - 1, self._y + self._length + 1)}
        if ship._tp == 1:
            coords2 = {(x, ship._y) for x in range(ship._x, ship._x + ship._length)}
        if ship._tp == 2:
            coords2 = {(ship._x, y) for y in range(ship._y, ship._y + ship._length)}
        # print(coords2&coords1)
        return bool(coords2 & coords1)

    def is_out_pole(self, size):
        pos1 = self._x, self._y
        if self._tp == 1:
            pos2 = (self._x + self._length - 1, self._y)
        if self._tp == 2:
            pos2 = (self._x, self._y + self._length - 1)
        # print(pos1 + pos2)
        if any(map(lambda x: not (x in range(size)), pos1 + pos2)):
            return True
        return False

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []
        self._pole = [[0] * size for _ in range(size)]

    def init(self):
        # self._ships = [Ship(4, tp=randint(1, 2))]
        self._ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2))]
        while True:
            flag2 = True
            ships_ready = []

            for ship in self._ships:
                flag = True
                i = 0
                while flag:
                    flag = False
                    ship.set_start_coords(randint(0, self._size - 1), randint(0, self._size - 1))
                    if ship.is_out_pole(self._size):
                        flag = True
                    for ready_ship in ships_ready:
                        if ship.is_collide(ready_ship):
                            flag = True
                            break
                    i += 1
                    if i > 100:
                        # print(i)
                        flag2 = False
                        break
                ships_ready.append(ship)

            if flag2:
                break
            else:
                for ship in self._ships:
                    ship.set_start_coords(None, None)


    def show(self):
        pole = self.get_pole()
        row0 = "   "+ " ".join([chr(ord('a') + i) for i in range(self._size)])
        print(row0)
        for i, row in enumerate(pole):
            if i in range(9):
                print(i+1,'', end=' ')
            else:
                print(i+1, end=' ')
            print(*row)
        pass
    def get_ships(self):
        return self._ships
    def get_pole(self):
        self._pole = [[0] * self._size for _ in range(self._size)]

        for ship in self._ships:
            if ship._tp == 1:
                for x in range(ship._length):
                    self._pole[ship._y][ship._x + x] = ship[x]
            if ship._tp == 2:
                for y in range(ship._length):
                    self._pole[ship._y + y][ship._x] = ship[y]
        out = tuple([tuple(row) for row in self._pole])
        return out

    def move_ships(self):
        move = [-1, 1]
        for i, ship in enumerate(self._ships):
            newShip = copy.deepcopy(ship)
            m = random.choice(move)
            newShip.move(m)
            if any(map(lambda x: newShip.is_collide(x) if x is not ship else False, self._ships)) or newShip.is_out_pole(self._size):
                m = -1 if m == 1 else 1
                newShip = copy.deepcopy(ship)
                newShip.move(m)
                if any(map(lambda x: newShip.is_collide(x) if x is not ship else False,
                           self._ships)) or newShip.is_out_pole(self._size):
                    pass
                else:
                    self._ships[i] = newShip
            else:
                self._ships[i] = newShip


s = Ship(4, 1, 7, 1)
s2 = Ship(4, 1, 1, 4)
# print(s.is_out_pole(10))
# print(s2.is_collide(s))
s = GamePole(8)
s.init()
s.show()
s.move_ships()
s.show()

print(s.get_pole())