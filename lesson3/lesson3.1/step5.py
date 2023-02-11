class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)

    pass


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)

    pass


class LessonItem:
    def __init__(self, name, number_of_tasks, duration):
        self.title = name
        self.practices = number_of_tasks
        self.duration = duration

    def __setattr__(self, key, value):
        # print(key, type(value))
        if key == 'title' and not type(value) is str:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ['practices', 'duration'] and ((not (type(value) is int)) or value < 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)

    def __getattr__(self, item):
        if item not in self.__dict__:
            return False

    def __delattr__(self, item):
        if item in ['title', 'practices', 'duration']:
            pass
        else:
            super().__delattr__(item)

    pass


a = LessonItem("Урок 1", 8, 1000)
del a.duration
print(a.duration)
