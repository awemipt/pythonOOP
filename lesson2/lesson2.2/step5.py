class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is int and 0 <= width <= 10_000 :
            self.__width = width
            self.show()

    @property
    def height(self):
        return  self.__height

    @height.setter
    def height(self, height):
        if type(height) is int and 0 <= height <= 10_000:
            self.__height = height
            self.show()

win = WindowDlg('abc', 10, 10)
win.height = 20
win.width = 100