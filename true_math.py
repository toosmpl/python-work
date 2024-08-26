from math import inf
def true_divide(first, second):
    if second == 0:
        return inf
    result1 = first / second
    return result1
# print(true_divide(49,7))
# print(true_divide(15,0))