from __future__ import annotations


class Rect:
    def __init__(self, x, y, width, height):
        if any([type(x) not in (int, float), type(y) not in (int, float),
                type(width) not in (int, float), width < 0, type(height) not in (int, float), height < 0]):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect: Rect):
        if not (self._x + self._width < rect._x or rect._x + rect._width < self._x or \
                self._y + self._height < rect._y or rect._y + rect._height < self._y):
            raise TypeError('прямоугольники пересекаются')


def is_collision(r1, r2):
    try:
        r1.is_collision(r2)
    except TypeError:
        return True
    return False


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = [lst_rect[i] for i in range(len(lst_rect))
                     if not any(is_collision(lst_rect[i], lst_rect[j])for j in range(len(lst_rect)) if i != j)]
