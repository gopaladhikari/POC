# Method Resolution Order (MRO)


class A:
    label = "A"


class B(A):
    label = "B"


class C(A):
    label = "C"


class D(C, B):
    pass


cup = D()

print(cup.label)
print(D.__mro__)
