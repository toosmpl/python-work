data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def structure (*data_structure):
    sumator = 0
    for i in data_structure:
        if isinstance(i, (list, tuple, set)):
            sumator += structure(*i)
        elif isinstance(i, (dict)):
            sumator += structure(*i.items())
        elif isinstance(i, str):
            sumator += len(i)
        elif isinstance(i, int):
            sumator += i
    return sumator



print(structure(data_structure))


