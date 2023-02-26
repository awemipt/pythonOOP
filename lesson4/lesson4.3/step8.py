class SoftList(list):
    def __getitem__(self, item):
        try:
            x = super().__getitem__(item)
        except IndexError:
            return False
        return x


print(SoftList([1])[2])
