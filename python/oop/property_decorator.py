class TeaLeaf:
    def __init__(self, age) -> None:
        self._age = age

    @property
    def age(self):
        return self._age + 2

    @age.setter
    def age(self, value):
        if 1 <= value <= 10:
            self._age = value
        else:
            raise ValueError("Age must be between 1 and 10")


leaf = TeaLeaf(5)
print(leaf.age)
# leaf.age = 17 Error
