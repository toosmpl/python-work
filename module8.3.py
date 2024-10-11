class Car():
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int):
            if 1000000 > vin_number or vin_number > 9999999:
                raise IncorrectVinNumber('Не верный диапозон')
            elif vin_number is False:
                return True
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            if len(numbers) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')
            elif numbers == 0:
                return True
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
