def square(x):
    return x * x


cube = lambda x: x * square(x)

print(cube(3))


sum = lambda x, y: x + y
print(sum(1, 2))


custom_sum = lambda a, b, c: a + b + c

print(custom_sum(1, 3, 5))
