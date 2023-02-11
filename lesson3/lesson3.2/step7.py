class HandlerGET:
    def __init__(self, func):
        self.fn = func

    def get(self, func, request, *args, **kwargs):
        res = ''
        if request.get('method', 'GET') == 'GET':
            res += 'GET: '
            res += func(request)
        else:
            return None
        return res

    def __call__(self, *args, **kwargs):
        return self.get(self.fn, args[0])


@HandlerGet
def contact(request):
    return "Сергей Балакирев"


print(contact({"method": "GET", "url": "contact.html"}))
