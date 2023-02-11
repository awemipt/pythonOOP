class PhoneBook:
    def __init__(self):
        self.phonelist = []

    def add_phone(self, phone):
        self.phonelist.append(phone)

    def remove_phone(self, indx):
        self.phonelist.pop(indx)
    def get_phone_list(self):
        return self.phonelist

class PhoneNumber:
    def __init__(self, number, fio):
        self.fio = fio
        self.number = number

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)