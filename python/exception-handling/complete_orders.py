class InvalidTeaError(Exception):
    pass


def bill(flavor, cups):
    menu = {
        "masala": 100,
        "green": 50,
        "oolong": 80,
        "black": 60,
        "milk": 20,
        "lemon": 30,
        "peach": 40,
    }

    try:
        if flavor not in menu:
            raise InvalidTeaError(f"{flavor} is not available")

        if not isinstance(cups, int):
            raise TypeError("Number of cups must be integer")

        return f"Price of {flavor} is {menu[flavor] * cups}"

    except InvalidTeaError as e:
        return e

    except TypeError as e:
        return e


print(bill("masala", 2))
print(bill("coffee", 8))
print(bill("masala", "eight"))
