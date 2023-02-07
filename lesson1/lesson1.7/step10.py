class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked



class AppStore:
    apps = []
    def add_application(self, app: Application):
        self.apps.append(app)

    def remove_application(self, app:Application):
        del self.apps[self.apps.index(app)]

    def block_application(self,app:Application):
        app.blocked = True

    def total_apps(self):
        return len(self.apps)

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
print(store.total_apps())
store.remove_application(app_youtube)
print(store.total_apps())
