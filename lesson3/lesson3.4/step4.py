class NewList:
    def __init__(self, lst=None):
        if lst:
            self.lst = lst
        else:
            self.lst = []

    def get_list(self):
        return self.lst

    @staticmethod
    def __list_diff(x, l2):
        for val in l2:
            if str(x) == str(val):
                l2.remove(x)
                return False
        return True

    def __sub__(self, other):
        l1 = self.lst[:]
        if type(other) == NewList:
            other = other.lst
        l2 = other[:]
        ans = [x for x in l1 if self.__list_diff(x, l2)]
        return NewList(ans)

    def __rsub__(self, other):
        l1 = self.lst[:]
        if isinstance(other, NewList):
            other = other.lst
        l2 = other[:]
        ans = [x for x in l2 if self.__list_diff(x, l1)]
        return NewList(ans)

    def __isub__(self, other):
        l1 = self.lst[:]
        if type(other) == NewList:
            other = other.lst
        l2 = other[:]
        ans = [x for x in l1 if self.__list_diff(x, l2)]
        self.lst = ans
        return self
    pass


lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

# res1 = lst1 - lst2
lst1 -= lst2
print(lst1.get_list())
