class DigitRetrieve:
    def __call__(self, num, *args, **kwargs):
        fl = 1
        if num[0] == "-":
            num = num[1:]
            fl = -1
        if num.isdigit():
            return fl*int(num)
        return None

dg = DigitRetrieve()

st = ["123", "abc", "--56.4", "0", "-5"]
digits = list(map(dg, st))
print(digits)