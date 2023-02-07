from typing import List


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


class Viber:
    messages: List[Message] = []
    @classmethod
    def add_message(cls, msg: Message):
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg: Message):
        cls.messages.remove(msg)

    @classmethod
    def set_like(cls, msg: Message):
        msg.fl_like ^= True

    @classmethod
    def show_last_message(cls, n: int):
        print(*[x.text for x in cls.messages[-n:]])

    @classmethod
    def total_messages(cls):
        return len(cls.messages)

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)