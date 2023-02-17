import random


class Cell:
    def __init__(self, value=0):
        self.value = value
        self.is_free = True
        if self.value:
            self.is_free = False

    def __bool__(self):
        return self.value == 0

    def __eq__(self, other):
        return self.value == other.value


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2
    showPole = {FREE_CELL: '*', HUMAN_X: 'X', COMPUTER_O: 'O'}
    HUMAN_WIN = tuple([Cell(HUMAN_X), Cell(HUMAN_X), Cell(HUMAN_X)])
    COMPUTER_WIN = tuple([Cell(COMPUTER_O), Cell(COMPUTER_O), Cell(COMPUTER_O)])

    def __init__(self):
        self.pole = tuple([tuple([Cell() for i in range(3)]) for j in range(3)])

    def init(self):
        self.clear()

    def show(self):
        print('  1 2 3')
        for i in range(3):
            print(i + 1, end=' ')
            for j in range(3):
                print(self.showPole[self.pole[i][j].value], end=' ')
            print()

    def human_go(self):
        i, j = map(int, input('Введите координаты клетки через пробел').split())
        i -= 1
        j -= 1
        while not self.pole[i][j]:
            i, j = map(int, input('Занято, Введите координаты клетки через пробел').split())
            i -= 1
            j -= 1
        self.pole[i][j].value = self.HUMAN_X
        self.pole[i][j].is_free = False

    def computer_go(self):
        i, j = random.randint(1, 3), random.randint(1, 3)
        i -= 1
        j -= 1
        while not self.pole[i][j]:
            i, j = random.randint(1, 3), random.randint(1, 3)
            i -= 1
            j -= 1
        self.pole[i][j].value = self.COMPUTER_O
        self.pole[i][j].is_free = False

    @property
    def is_human_win(self):
        for i in range(3):
            if self.pole[i] == self.HUMAN_WIN:
                return True
        for j in range(3):
            ans = ()
            for row in self.pole:
                ans += row[j],
            if ans == self.HUMAN_WIN:
                return True
        diag1 = self.pole[0][0], self.pole[1][1], self.pole[2][2]
        if diag1 == self.HUMAN_WIN:
            return True
        diag2 = self.pole[2][0], self.pole[1][1], self.pole[0][2]
        if diag2 == self.HUMAN_WIN:
            return True
        return False

    @property
    def is_computer_win(self):
        for i in range(3):
            if self.pole[i] == self.COMPUTER_WIN:
                return True
        for j in range(3):
            ans = ()
            for row in self.pole:
                ans += row[j],
            if ans == self.COMPUTER_WIN:
                return True
        diag1 = self.pole[0][0], self.pole[1][1], self.pole[2][2]
        if diag1 == self.COMPUTER_WIN:
            return True
        diag2 = self.pole[2][0], self.pole[1][1], self.pole[0][2]
        if diag2 == self.COMPUTER_WIN:
            return True
        return False

    def is_free(self):
        for i in range(3):
            for j in range(3):
                if self.pole[i][j].is_free:
                    return True
        return False

    @property
    def is_draw(self):
        if not self.is_free() and not self.is_computer_win and not self.is_human_win:
            return True
        return False

    def __bool__(self):
        if self.is_draw or self.is_computer_win or self.is_human_win:
            return False
        return True




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
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")