a = 10
b = 20


def add(x, y):
    return x + y


print(add(a, b))


def subtract(x, y):
    return x - y


print(subtract(a, b))


def multiply(x, y):
    return x * y


print(multiply(a, b))


def divide(x, y):
    return x / y


print(divide(a, b))


def power(x, y):
    return x**y


print(power(a, b))


def square(x):
    return x**2


print(square(a))


def cube(x):
    return x**3


print(cube(a))


def square_root(x):
    return x**0.5


print(square_root(a))


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(a))
