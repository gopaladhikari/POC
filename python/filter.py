def is_even(x):
    return x % 2 == 0


l = [1, 2, 3, 4, 5]

evens = list(filter(is_even, l))

print(evens)
