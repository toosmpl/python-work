from threading import Thread
from time import sleep


class Knight(Thread):
    threads = 100
    days = 0

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на нас напали')
        while self.threads != 0:
            sleep(1)
            self.days += 1
            self.threads = self.threads - self.power
            print(f'{self.name} сражается {self.days}..., осталось {self.threads} воинов.')
        print(f'{self.name}одержал победу спустя {self.days} дней(дня)')



# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')