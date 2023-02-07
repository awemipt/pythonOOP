class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


import sys

# здесь объявляются все необходимые классы

# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять

# здесь создаются объекты классов и вызываются нужные методы
head_obj = ListObject(lst_in[0])
tmp = head_obj
for line in lst_in[1:]:
    tmp2 = ListObject(line)
    tmp.link(tmp2)
    tmp = tmp2


