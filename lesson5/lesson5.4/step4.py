class StringException(Exception):
    pass

class NegativeLengthString(StringException):
    pass

class ExceedLengthString(StringException):
    pass

# здесь объявляйте классы


try:
    raise ExceedLengthString
    # здесь команда для генерации исключения
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")