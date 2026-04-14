class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, value):
        return self.value + value.value


n = Number(10)

m = Number(20)


print(n + m)
