class Descr:
    def __set_name__(self, owner, name):
        self.name = '_' +owner.__name__+'__'+ name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class ObjList:
    data = Descr()
    prev = Descr()
    next = Descr()

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    # @property
    # def data(self):
    #     return self.__data
    #
    # @data.setter
    # def data(self, value):
    #     self.__data = value
    #
    # @property
    # def prev(self):
    #     return self.__prev
    #
    # @prev.setter
    # def prev(self, value):
    #     self.__prev = value
    #
    # @property
    # def next(self):
    #     return self.__next
    #
    # @next.setter
    # def next(self, value):
    #     self.__next = value



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_obj(self, obj):
        self.length += 1
        if not self.head:
            self.tail = obj
            self.head = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj
        # print(self.head.data)

    def remove_obj(self, indx):
        self.length -= 1
        obj = self.head
        if indx == 0:
            if self.length == 0:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        for i in range(indx):
            obj = obj.next
        if obj.next is None:
            self.tail = obj.prev
            self.tail.next = None
        else:
            obj.prev.next, obj.next.prev = obj.next, obj.zprev

    def __len__(self):
        return self.length

    def __call__(self, indx, *args, **kwargs):
        obj = self.head
        for i in range(indx):
            obj = obj.next
        return obj.data
        pass


linked_lst = LinkedList()
a = ObjList('a')
print(a.__dict__)
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.add_obj(ObjList("Python ООП"))
linked_lst.remove_obj(0)
linked_lst.remove_obj(0)

print(len(linked_lst))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev
print(s, n)
