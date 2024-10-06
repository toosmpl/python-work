def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    corret_data = 0
    for number in numbers:
        try:
            result += number
            corret_data += 1
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1
    return result, incorrect_data, corret_data


def calculate_average(numbers):
    try:
        sum_numbers = personal_sum(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    try:
        average = sum_numbers[0] / sum_numbers[2]
    except ZeroDivisionError:
        return 0
    return average


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать