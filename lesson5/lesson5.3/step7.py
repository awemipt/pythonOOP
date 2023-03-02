class TupleLimit(tuple):
    def __new__(cls, *args, **kwargs):
        if len(args[0]) > args[1]:
            raise ValueError('число элементов коллекции превышает заданный предел')
        instance = super().__new__(cls, args[0])

        return instance

    def __repr__(self):
        return " ".join(map(lambda x: str(float(x)), self))

    def __str__(self):
        return " ".join(map(lambda x: str(float(x)), self))


digits = list(map(float, input().split()))
try:
    x = TupleLimit(digits, 5)
    print(x)
except Exception as e:
    print(e)
