from typing import List, Any


class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class CellInteger:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) is not int or not self._min_value <= value <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')
        self._value = value


class CellFloat:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) is not float or not self._min_value <= value <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')
        self._value = value


class CellString:
    def __init__(self, min_length, max_length):
        self._min_length = min_length
        self._max_length = max_length
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) is not str or not self._min_length <= len(value) <= self._max_length:
            raise CellStringException('длина строки выходит за допустимый диапазон')
        self._value = value


class TupleData:
    def __init__(self, *args):
        if any(map(lambda x: type(x) not in (CellString, CellFloat, CellInteger), args)):
            raise Exception('Все аргументы должны быть Cell')
        self.cells: List[Any[CellString, CellFloat, CellInteger]] = list(args)

    def check_indx(self, indx):
        if type(indx) is not int or not 0 <= indx <= len(self.cells):
            raise IndexError

    def __getitem__(self, item):
        self.check_indx(item)
        return self.cells[item].value

    def __setitem__(self, key, value):
        self.check_indx(key)
        self.cells[key].value = value

    def __len__(self):
        return len(self.cells)

    def __iter__(self):
        for cell in self.cells:
            yield cell.value


ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
