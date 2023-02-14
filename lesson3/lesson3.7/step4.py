class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0

import sys

# считывание списка из входного потока (эту строчку и список lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))
players = [Player(row.split('; ')[0], int(row.split('; ')[1]), int(row.split('; ')[2])) for row in lst_in]
players_filtered = list(filter(bool, players))
