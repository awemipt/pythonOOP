class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []
        self.classes = []

    def add_app(self, app):
        if app.__class__ not in self.classes:
            self.apps.append(app)
            self.classes.append(app.__class__)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = 'ВКонтакте'


class AppYouTube:
    def __init__(self, memory):
        self.name = 'YouTube'
        self.memory = memory


class AppPhone:
    def __init__(self, phone_list):
        self.name = 'Phone'
        self.phone_list = phone_list


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
print(type('1'))