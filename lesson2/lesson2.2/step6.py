class StackObj:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if type(next) is StackObj or next is None:
            self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj: StackObj):
        if self.top is None:
            self.top = obj
        else:
            tmp = self.top
            while tmp.next:
                tmp = tmp.next
            tmp.next = obj

    def pop(self):

        tmp = self.top
        if tmp is None:
            return None
        if tmp.next is None:
            self.top = None
            return tmp
        while tmp.next:
            prev = tmp
            tmp = tmp.next
        prev.next = None
        return tmp

    def get_data(self):
        ans = []
        tmp = self.top
        while tmp:
            ans.append(tmp.data)
            tmp = tmp.next
        return ans

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
st.pop()
st.pop()
res = st.get_data()
print(res)