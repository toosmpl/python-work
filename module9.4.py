import random
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)


def get_advanced_write(file_name):

    def write_everything(*data_set):
        with open(file_name, mode='w', encoding='UTF-8') as file:
            for elements in data_set:
                file.write(str(elements))
                file.write('\n')
            return data_set
    return write_everything

write = get_advanced_write('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall():
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        words = choice(self.words)
        return words

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())