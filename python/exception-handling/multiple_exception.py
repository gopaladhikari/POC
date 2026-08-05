def process_order(order, quantity):
    try:
        price = {"green": 10}[order]
        cost = price * quantity
        print(f"Cost of {quantity} {order} is {cost}")
    except KeyError as e:
        print(f"{e} is not available")
    except TypeError as e:
        print("Quantity must be integer")
    except Exception as e:
        print("Something went wrong")


process_order("green", "2")
process_order("red", 2)
process_order("red", "2")
