class WordString:
    def __init__(self, *args):
        self.string = ''
        if args:
            self.string = args[0]

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value: str):
        # while value.find('  ') != -1:
        #     value = value.replace('  ', ' ')
        self.__string = value
        self.__words = value.split()

    def __len__(self):
        return len(self.__words)

    def __call__(self,indx, *args, **kwargs):
        return self.__words[indx]



words = WordString()
words.string = "Курс   по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")