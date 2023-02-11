class Handler:
    def __init__(self, methods=('GET',)):
        self.__methods = methods

    def get(self, func, request, *args, **kwargs):
        res = ''
        print('a')
        if request.get('method', 'GET') == 'GET':
            res += 'GET: '
            res += func(request)
        else:
            return None
        return res

    def post(self, func, request, *args, **kwargs):
        res = ''
        if request.get('method', 'POST') == 'POST':
            res += 'POST: '
            res += func(request)
        else:
            return None
        return res

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            m = request.get('method', 'GET')
            if m in self.__methods:
                method = m.lower()

                return self.__getattribute__(method)(func, request)

        return wrapper


@Handler(("POST",'GET'))
def contact(request):
    return "Сергей Балакирев"


print(contact({"method": "GET", "url": "contact.html"}))
