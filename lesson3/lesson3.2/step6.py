class RenderList:
    def __init__(self, type_list):
        self.__type_list = 'ol' if type_list == 'ol' else 'ul'

    def __call__(self, *args, **kwargs):
        text = ''
        for line in args[0]:
            text += '<li>' + line + '</li>\n'
        return f'<{self.__type_list}>\n' + text +\
               f'</{self.__type_list}>\n'

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)