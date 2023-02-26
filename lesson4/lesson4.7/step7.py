class Note:
    NOTES = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
    TONES = [-1, 0, 1]

    def __init__(self, name, ton=0):
        if name not in self.NOTES or ton not in self.TONES:
            raise ValueError('недопустимое значение аргумента')
        self._name = name
        self._ton = ton
    def __setattr__(self, key, value):
        if key == '_name':
            if value not in self.NOTES:
                raise ValueError('недопустимое значение аргумента')
        if key == '_ton':
            if value not in self.TONES:
                raise ValueError('недопустимое значение аргумента')
        super().__setattr__(key, value)

class Notes:
    __slots__ = ['_do', '_re', '_mi', '_fa', '_solt', '_la', '_si']
    INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if cls.INSTANCE is None:
            cls.INSTANCE = super().__new__(cls)
        return cls.INSTANCE

    def __init__(self):
        self._do = Note('до')
        self._re = Note('ре')
        self._mi = Note('ми')
        self._fa = Note('фа')
        self._solt = Note('соль')
        self._la = Note('ля')
        self._si = Note('си')

    def __getitem__(self, item):
        try:
            return getattr(self, self.__slots__[item])
        except IndexError:
            raise IndexError('недопустимый индекс')

notes = Notes()
notes[0]._ton = -2