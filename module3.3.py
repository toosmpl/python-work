def print_params(a=1, b='строка', c=True):
    print(a, b, c, )
    b = 25
    c = [1, 2, 3]


value_list = [1, 'string', True]
value_dict = {'a': 1, 'b': 'dict', 'c': False}
value_list2 = [54.32, 'cтрока']

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*value_list)
print_params(**value_dict)
print_params(*value_list2, 42)
