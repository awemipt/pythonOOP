class descr:
    def __set_name__(self, owner, name):
        self.name = '_' + owner.__name__ + "__" + name

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class StackObj:
    data = descr()
    prev = descr()
    next = descr()

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        tmp = self.top
        if self.top is None:
            self.top = obj
            return
        while not (tmp.next is None):
            tmp = tmp.next
        tmp.next = obj

    def pop_back(self):
        tmp = self.top
        if tmp.next is None:
            self.top = None
            return
        while tmp.next.next:
            tmp = tmp.next
        tmp.next = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self

    def print_data(self):
        tmp = self.top
        ans = []
        while tmp:
            ans.append(tmp.data)
            tmp = tmp.next
        return ans

st = Stack()
st.push_back(StackObj('1'))
st.push_back(StackObj('2'))
st.push_back(StackObj('3'))
st.push_back(StackObj('4'))
st += StackObj('5')
print((st * list(range(10))).print_data())
print(st.print_data())