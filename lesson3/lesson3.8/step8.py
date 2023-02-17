class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free


class TicTacToe:
    def __init__(self):
        self.pole = tuple([tuple([Cell() for i in range(3)]) for j in range(3)])

    def __getitem__(self, item):
        i, j = item
        if type(i) == slice and type(j) == int:
            tmp = []
            for line in self.pole:
                tmp.append(line[j].value)
            return tuple(tmp[i])

        elif type(j) == slice and type(i) == int:
            return tuple([x.value for x in self.pole[i][j]])
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        i, j = key
        if any([i < 0, j < 0, i >= 3, j >= 3]):
            raise IndexError('неверный индекс клетки')
        if not self.pole[i][j]:
            raise ValueError('клетка уже занята')
        self.pole[i][j].value = value
        self.pole[i][j].is_free = False

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].value = 0
                self.pole[i][j].is_free = True


game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
# game[3, 2] = 2 # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2

v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0
print(v2)
