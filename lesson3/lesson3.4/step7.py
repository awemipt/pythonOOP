class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if type(other) is int:
            self.book_list.pop(other)
        elif type(other) is Book:
            if other in self.book_list:
                self.book_list.remove(other)
        return self

    def __len__(self):
        return len(self.book_list)
