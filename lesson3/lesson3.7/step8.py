import random


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = True

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")

        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if type(value) != int or not( 0 <= value <= 8):
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")

        self.__is_open = value

    def __bool__(self):
        return not self.__is_open


class GamePole:
    one = None

    def __new__(cls, *args, **kwargs):

        if cls.one is None:
            cls.one = super().__new__(cls)
        return cls.one

    @property
    def pole(self):
        return self.__pole_cells

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.coords = {(i, j) for i in range(N) for j in range(M)}
        self.__pole_cells = tuple([tuple([Cell() for j in range(M)]) for i in range(N)])
        self.init_pole()
        # self.show_pole()

    def init_pole(self):
        mines = random.sample(sorted(self.coords), self.total_mines)
        print(self.total_mines)
        for mine in mines:
            self.__pole_cells[mine[0]][mine[1]].is_mine = True
        for i in range(self.N):
            for j in range(self.M):
                if not self.__pole_cells[i][j].is_mine:
                    num = 0
                    for i1 in range(max(0, i - 1), min(self.N, i + 2)):
                        for j1 in range(max(0, j - 1), min(self.M, j + 2)):
                            if self.__pole_cells[i1][j1].is_mine:
                                num += 1
                    self.__pole_cells[i][j].number = num

    def show_pole(self):
        for i in range(self.N):
            for j in range(self.M):
                if self.__pole_cells[i][j]:
                    print('#', end=' ')
                elif self.__pole_cells[i][j].is_mine:
                    print('*', end=' ')
                else:
                    print(self.__pole_cells[i][j].number, end=' ')
            print()

    def open_cell(self, i, j):
        if 0 <= i < self.N and 0 <= j <self.M:
            self.__pole_cells[i][j].is_open = True

        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

pole = GamePole(5, 5, 10)  # создается поле размерами 10x20 с общим числом мин 10

if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][4]:
    pole.open_cell(3, 4) # генерируется исключение IndexError
pole.show_pole()
cell = Cell()
