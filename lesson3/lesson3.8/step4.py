class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if type(value) != int:
            raise ValueError('должно быть целое число')
        self.__value = value


class Array:
    def __init__(self, max_length, cell):
        self.lst = [cell() for x in range( max_length)]

    def __str__(self):
        return " ".join([str(x.value) for x in self.lst])

    def __check_indx(self, indx):
        if indx < 0 or indx >= len(self.lst):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.__check_indx(item)
        return self.lst[item].value

    def __setitem__(self, key, value):
        self.__check_indx(key)
        self.lst[key].value = value

ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
print(ar_int)
ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[10] = 1 # должно генерироваться исключение IndexError