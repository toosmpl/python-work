def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for line, string in enumerate(strings, start=1):
            byte = file.tell()
            file.write(string + '\n')
            strings_positions[(line, byte)] = string

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('tesfgdfgst.txt', info)
for elem in result.items():
    print(elem)