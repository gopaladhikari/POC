tea_menu = {
    "masala": 100,
    "green": 50,
    "oolong": 80,
    "black": 60,
    "milk": 20,
    "lemon": 30,
    "peach": 40,
}

try:
    print(tea_menu["coffee"])
except KeyError as e:
    print(e)


def serve(flavor):
    try:
        print(f"serving {flavor} tea at {tea_menu[flavor]}")
    except KeyError as e:
        print(f"{e} is not available")
    else:
        print(f"{flavor} tea served")
    finally:
        print("Thanks for visiting")


serve("masala")
serve("coffee")
