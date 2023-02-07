# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
            return 1
        if self.a < 0 or self.b < 0 or self.c < 0:
            return 1
        lst = sorted((self.a, self.b, self.c))
        if lst[0] + lst[1] <= lst[2]:
            return 2
        return 3


a, b, c = map(int, input().split())  # эту строчку не менять
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
