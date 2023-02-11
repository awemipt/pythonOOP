class ObjList:
    def __init__(self, data, next=None, prev=None):
        self.__data = data
        self.__next = next
        self.__prev = prev

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList):
        if self.head is None:
            self.head = obj
            self.tail = obj
            obj.set_prev(None)
            obj.set_next(None)
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        if self.tail is None:
            self.head = None
            return
        self.tail = self.tail.get_prev()
        if self.tail is None:
            self.head = None
            return
        self.tail.set_next(None)

    def get_data(self):
        head = self.head
        ans = []
        while not head is None:
            ans.append(head.get_data())
            head = head.get_next()
        return ans

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
lst.remove_obj()
lst.remove_obj()

res = lst.get_data()
print(*res)