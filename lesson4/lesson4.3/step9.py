class StringDigit(str):
    def __init__(self, string: str):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")
        # super().__init__()

    def __add__(self, other):
        if not other.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return StringDigit(super().__add__(other))

    def __radd__(self, other):
        if not other.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return StringDigit(str(other) + str(self))


sd = StringDigit("123")
print(sd)
sd = sd + "456"  # StringDigit: 123456
sd = "789" + sd  # StringDigit: 789123456
print(sd)  # 123

sd = sd + "12"
