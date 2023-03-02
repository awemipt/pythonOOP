class Test:
    def __init__(self, descr):

        if not 10 <= len(descr) <= 10000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self._descr = descr


    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        if type(ans_digit) not in (int, float) or type(max_error_digit) not in (int, float) or max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')
        super().__init__(descr)
        self._ans_digit = ans_digit
        self._max_error_digit = max_error_digit


    def run(self):
        ans = float(input())
        return self._ans_digit - self._max_error_digit <= ans <= self._ans_digit + self._max_error_digit


descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans)  # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
try:
    t = TestAnsDigit(descr, ans)
    print(t.run())
except Exception as e:
    print(e)
