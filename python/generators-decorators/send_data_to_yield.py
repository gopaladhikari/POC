def customer():
    print("Welcome to our store ! Which product you want to buy ?")

    order = yield

    while True:

        print(f"Your order is {order}")

        order = yield


stall = customer()

next(stall)

stall.send("Milk")


stall.send("Lemon")
