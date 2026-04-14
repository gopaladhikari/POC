# Set = Unordered collection of unique elements

s = {1, 2, 3}
t = {1, 56}

empty = set()  # Empty set

# Set methods


print(s.union(t))
print(s.intersection(t))

s.add(4)
print(s)

s.remove(2)
print(s)

s.discard(3)
print(s)

s.clear()
print(s)
