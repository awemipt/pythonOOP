import sys

# здесь объявляйте класс
class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in не менять!
books = [BookStudy(*row.split('; ')) for row in lst_in]
unique_books = len(set([hash(book) for book in books]))
print(unique_books)