class StringText:
    def __init__(self, lst_words):
        self.lst = lst_words

    def __lt__(self, other):
        return len(self.lst) < len(other.lst)

    def __le__(self, other):
        return len(self.lst) <= len(other.lst)

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

lst_text = [StringText(line.strip("–?!,.;").split()) for line in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [" ".join(row.lst) for row in lst_text_sorted]
print(lst_text_sorted)