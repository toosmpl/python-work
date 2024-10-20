def is_prime(func):
    def wrapper(*args):
        prime = func(*args)
        if prime % 2 == 0:
            print('Составное')
        else:
            print('Простое')
        return prime
    return wrapper

@is_prime
def sum_three(*args):
    res = sum(args)
    return res


result = sum_three(2, 3, 6)
print(result)
