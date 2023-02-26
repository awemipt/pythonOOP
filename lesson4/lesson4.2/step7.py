class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()

class VideoRating:
    def __init__(self):
        self.__rating = 0
    @staticmethod
    def __check_rating(value):
        if type(value) is not int or value < 0 or value > 5:
            raise ValueError('неверное присваиваемое значение')

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__check_rating(value)
        self.__rating = value


v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
# v.rating.rating = 6  # ValueError