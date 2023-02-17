class descr:
    def __set_name__(self, owner, name):
        self.name = '_' + owner.__name__ + "__" + name

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class StackObj:
    data = descr()
    next = descr()

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data}, {self.next}'

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, obj):
        self.length += 1
        tmp = self.top
        if self.top is None:
            self.top = obj
            return
        while not (tmp.next is None):
            tmp = tmp.next
        tmp.next = obj

    def pop(self):
        if self.length > 0:
            self.length -= 1
        tmp = self.top
        if tmp.next is None:
            self.top = None
            return
        while tmp.next.next:
            tmp = tmp.next

        tmp2  = tmp.next
        tmp.next = None
        return tmp2

    # def __add__(self, other):
    #     self.push_back(other)
    #     return self
    #
    # def __mul__(self, other):
    #     for i in other:
    #         self.push_back(StackObj(i))
    #     return self

    def print_data(self):
        tmp = self.top
        ans = []
        while tmp:
            ans.append(tmp.data)
            tmp = tmp.next
        return ans

    def __check_indx(self, indx):
        if indx < 0 or indx >= self.length:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_indx(item)
        tmp = self.top
        for i in range(item):
            tmp = tmp.next
        return tmp

    def __setitem__(self, key, value):
        self.__check_indx(key)
        if key == 0:
            tmp = self.top
            self.head = value
            self.head.next = tmp.next
        else:
            tmp = self.top
            for i in range(key - 1):
                tmp = tmp.next
            tmp2 = tmp.next
            tmp.next = value
            tmp.next.next = tmp2.next


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data)  # obj3
print(st[0])  # new obj2
# res = st[3]  # исключение IndexError
