import random


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.coords = [(i, j) for i in range(self.N) for j in range(self.N)]
        # self.coords = [(1,1)]
        self.init()

    def init(self):
        self.pole = []
        mines = set(random.sample(self.coords, self.M))
        row = []
        for i in range(self.N):
            for j in range(self.N):
                if (i, j) in mines:
                    row.append(Cell(mine=True))
                else:
                    row.append(Cell())
            self.pole.append(row)
            row = []
        for i in range(self.N):
            for j in range(self.N):
                self.pole[i][j].around_mines = self.count_mines(i, j)

    def count_mines(self, i, j):
        count = 0
        for row in range(max(i - 1, 0), min(i + 2, self.N)):
            for col in range(max(j - 1, 0), min(j + 2, self.N)):
                if  row != i or col != j:
                    if self.pole[row][col].mine:
                        count += 1
        return count

    def show(self):
        for row in self.pole:
            for mine in row:
                print('#' if not mine.fl_open else '*' if mine.mine else mine.around_mines, end=' ')
            print()


pole_game = GamePole(10, 12)
pole_game.show()
