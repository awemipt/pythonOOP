class descr:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


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

    def push_back(self, obj):
        self.length += 1
        tmp = self.top
        if self.top is None:
            self.top = obj
            return
        while not (tmp.next is None):
            tmp = tmp.next
        tmp.next = obj
    def push_front(self, obj):
        self.length += 1
        tmp = self.top
        self.top = obj
        obj.next = tmp
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
        return tmp.data

    def __setitem__(self, key, value):
        self.__check_indx(key)
        tmp = self.top
        for i in range(key):
            tmp = tmp.next
        tmp.data = value

    def __len__(self):
        return self.length

    def __iter__(self):
        tmp = self.top
        for i in range(self.length):
            prev = tmp
            tmp = tmp.next
            yield prev


st = Stack()
st.push_back(StackObj("obj1"))
st.push_back(StackObj("obj2"))
st.push_back(StackObj("obj3"))
st[1] = 'newObj2'
for i in st:
    print(i.data)



