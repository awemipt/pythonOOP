class Aircraft:
    @staticmethod
    def _check_str(value):
        if type(value) is not str:
            raise TypeError('неверный тип аргумента')

    @staticmethod
    def _check_digit(value):
        if type(value) not in (int, float) or value < 0:
            raise TypeError('неверный тип аргумента')

    def __init__(self, model, mass, speed, top):
        self._check_str(model)
        self._check_digit(mass)
        self._check_digit(speed)
        self._check_digit(top)
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top


class PassengerAircraft(Aircraft):
    @staticmethod
    def _check_int(value):
        if type(value) is not int or value < 0:
            raise TypeError('неверный тип аргумента')


    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._check_int(chairs)
        self._chairs = chairs


class WarPlane(Aircraft):
    @staticmethod
    def _check_dict(value):
        if type(value) is not dict:
            raise TypeError('неверный тип аргумента')

    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._check_dict(weapons)
        self._weapons = weapons


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane( 'Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane( 'Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]