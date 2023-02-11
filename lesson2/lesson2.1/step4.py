class Money:
    def __init__(self, money=0):
        if self.__check_money(money):
            self.__money = money

    @classmethod
    def __check_money(cls, money):
        if type(money) is int and money > 0:
            return True

        return False

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.__money

