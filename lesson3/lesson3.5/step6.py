class Morph:
    def __init__(self, *args):
        self.words = list(args)

    def add_word(self, word):
        self.words.append(word)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        return other.lower() in self.get_words()

dict_words = [Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'),
              Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]


text = input()
text = text.replace('.', ' ')
text = text.replace(',', ' ')
text = text.replace(';', ' ')
text = text.replace('?', ' ')
num = 0
for x in text.split():
    for mv in dict_words:
        if x == mv:
            num += 1
print(num)

