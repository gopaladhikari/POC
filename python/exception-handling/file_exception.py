file = open("order.txt", "w")

try:
    file.write("Orders for today")
finally:
    file.close()


with open("order.txt", "w") as file:
    file.write("Ginger ale")
