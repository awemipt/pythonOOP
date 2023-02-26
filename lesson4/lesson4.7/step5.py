class Planet:
    def __init__(self, name, diametr, period_solar, period):
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period


class SolarSystem:
    __slots__ = ['_mercury', '_venus', '_earth', '_mars',
                 '_jupiter', '_saturn', '_uranus', '_neptune']

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self._mercury = Planet(name='Меркурий', diametr=4878, period_solar=87.97, period=1407.5)
        self._venus = Planet(name='Венера', diametr=12104, period_solar=224.7, period=5832.45)
        self._earth = Planet(name='Земля', diametr=12756, period_solar=365.3, period=23.93)
        self._mars = Planet(name='Марс', diametr=6794, period_solar=687, period=24.62)
        self._jupiter = Planet(name='Юпитер', diametr=142800, period_solar=4330, period=9.9)
        self._saturn = Planet(name='Сатурн', diametr=120660, period_solar=10753, period=10.63)
        self._uranus = Planet(name='Уран', diametr=51118, period_solar=30665, period=17.2)
        self._neptune = Planet(name='Нептун', diametr=49528, period_solar=60150, period=16.1)


s = SolarSystem()