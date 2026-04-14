from functools import reduce


def sum(x, y):
    return x + y


print(reduce(sum, [1, 2, 3, 4, 5]))
