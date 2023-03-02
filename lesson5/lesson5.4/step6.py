class DateError(Exception):
    '''Ошибка даты'''


class DateString:
    @staticmethod
    def verify_day(day):
        if not 1 <= day <= 31:
            raise DateError

    @staticmethod
    def verify_month(month):
        if not 1 <= month <= 12:
            raise DateError

    @staticmethod
    def verify_year(year):
        if not 1 <= year <= 3000:
            raise DateError

    def __init__(self, date_string: str):
        if date_string.count('.') != 2:
            raise DateError
        day, month, year = date_string.split('.')
        try:
            self.day = int(day)
            self.month = int(month)
            self.year = int(year)
        except ValueError:
            raise DateError
        self.verify_year(self.year)
        self.verify_month(self.month)
        self.verify_day(self.day)

    def __str__(self):
        return f'{str(self.day).zfill(2)}.{str(self.month).zfill(2)}.{str(self.year).zfill(4)}'

date_string = input()

try:
    date = DateString(date_string)
    print(date)
except DateError:
    print("Неверный формат даты")