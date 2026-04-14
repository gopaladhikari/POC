def square(x):
    return x * x


cube = lambda x: x * square(x)

print(cube(3))


sum = lambda x, y: x + y
print(sum(1, 2))
