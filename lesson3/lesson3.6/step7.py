class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        if record not in self.dict_db:
            self.dict_db[record] = []
        self.dict_db[record].append(record)

    def read(self, pk):
        for key in self.dict_db:
            for record in self.dict_db[key]:
                if pk == record.pk:
                    return record


class Record:
    pk = 0

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.pk
        Record.pk += 1

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __repr__(self):
        return f'{self.fio}'


import sys

# здесь объявляйте классы

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in не менять!

# здесь продолжайте программу (используйте список строк lst_in)
db = DataBase('\\')
for row in lst_in:
    print(row)
    fio, descr, old = row.split('; ')
    record = Record(fio, descr, int(old))
    db.write(record)
print(db.dict_db)
