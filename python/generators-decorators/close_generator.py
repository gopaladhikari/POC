def get_users():
    yield {"id": 1, "name": "Gopal Adhikari"}
    yield {"id": 2, "name": "Shivam Sah"}
    yield {"id": 3, "name": "Rahul Tag"}


def get_admins():
    yield {"id": 1, "name": "Admin 1"}
    yield {"id": 2, "name": "Admin 2"}
    yield {"id": 3, "name": "Admin 3"}


def main():
    yield from get_users()
    yield from get_admins()


for user in main():
    print(user)


def tea_shop():
    try:
        while True:
            order = yield "Waiting for the order"
    except:
        print("Tea shop closed")


shop = tea_shop()

next(shop)

shop.send("Hot tea")
shop.send("Cold tea")

shop.close()  # Close the generator
