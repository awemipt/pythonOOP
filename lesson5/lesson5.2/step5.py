from decimal import Decimal


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

x, y = input().split()
try:
    x, y = int(x), int(y)
except ValueError:
    try:
        x, y = float(x), float(y)
    except ValueError:
        pt = Point()
    else:
        pt = Point(x, y)
else:
    pt = Point(x, y)

finally:
    print(f"Point: x = {pt._x}, y = {pt._y}")

