from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    CHARS_FOR_NUMBER = digits
    @classmethod
    def check_card_number(cls, number):
        nums = number.split('-')
        if len(nums) !=4:
            return False
        for num in nums:
            if len(num)!=4 or set(num) - set(cls.CHARS_FOR_NUMBER):
                return False

        return True

    @classmethod
    def check_name(cls, name:str):
        words = name.split(' ')
        if len(words) != 2:
            return False
        for word in words:
            if set(word) - set(cls.CHARS_FOR_NAME):
                return False

        return True



print( CardCheck.check_card_number("1234-5678-9012-0000"))
print(CardCheck.check_name("SERGEI BALAKIREV"))