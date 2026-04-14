a = 10

print(a)


def func():
    global a
    a = 2
    print(a)


print(a)

if __name__ == "__main__":
    func()
