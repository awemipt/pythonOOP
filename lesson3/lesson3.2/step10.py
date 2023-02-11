class InputValues:
    def __init__(self, render):  # render - ссылка на функцию или объект для преобразования
        self.render = render

    # здесь строчки программы

    def __call__(self, func):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return list(map(self.render, func(*args, **kwargs).split()))

        # здесь строчки программы
        return wrapper


class RenderDigit:
    def __call__(self, num, *args, **kwargs):
        try:
            return int(num)
        except:
            return None


render = RenderDigit()


@InputValues(render)
def input_dg():
    return input()


res = input_dg()
print(res)
