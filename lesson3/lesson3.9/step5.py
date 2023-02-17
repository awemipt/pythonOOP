class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.attrs = [fio, job, old, salary, year_job]

    def __check_indx(self, indx):
        if indx < 0 or indx > 4:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_indx(item)
        return self.attrs[item]

    def __setitem__(self, key, value):
        self.__check_indx(key)
        self.attrs[key] = value
        lst = list(self.__dict__)
        setattr(self, lst[key], value)
        self.indx = -1

    def __next__(self):
        if self.indx + 1 <= 4:
            self.indx += 1
            return self.attrs[self.indx]
        else:
            raise StopIteration

    def __iter__(self):
        self.indx = -1
        return self


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
print(pers.fio)

for i in pers:
    print(i)
for i in pers:
    print(i)
