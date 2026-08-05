menu = ["masala", "green", "oolong", "black", "milk", "lemon", "peach"]


def brew_tea(flavor):
    if flavor not in menu:
        raise ValueError("We don't have this flavor of tea")

    print(f"Brewing {flavor} tea")


brew_tea("coffee")
