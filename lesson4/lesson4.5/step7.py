from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if self._top is None:
            self._top = obj
        else:
            tmp = self._top
            while tmp._next:
                tmp = tmp._next
            tmp._next = obj

    def pop_back(self):
        if self._top is None:
            return self._top
        if self._top._next is None:
            obj, self._top =self._top, None
            return  obj
        tmp = self._top
        while tmp._next._next:
            tmp = tmp._next
        obj, tmp._next = tmp._next, None
        return obj

class StackObj:
    def __init__(self, data, next=None):
        self._data = data
        self._next = next

st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
