class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):

        if key in ['title', 'author']:
            if not type(value) is str:
                raise TypeError("Неверный тип присваиваемых данных.")
        if key in ['year', 'pages']:
            if not type(value) is int:
                raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)

book = Book( 'Python ООП','Сергей Балакирев', 123, 2022)
