class OutOfIngredients(Exception):
    pass


def make_tea(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredients("Out of ingredients")
    print("Making tea...")


make_tea(1, 0)
