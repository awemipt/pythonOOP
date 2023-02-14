class Body:
    def __init__(self, name, density, volume):
        self.name = name
        self.density = density
        self.volume = volume
    @classmethod
    def check_value(cls, value):
        if type(value) not in (Body, int):
            raise ArithmeticError()
        return value if type(value) is int else value.density * value.volume

    def __lt__(self, other):
        other = self.check_value(other)
        return self.volume * self.density < other

    def __eq__(self, other):
        other = self.check_value(other)
        return self.volume * self.density == other
