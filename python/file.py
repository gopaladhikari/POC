f = open("file.txt")

data = f.read()

print(data)

f.close()

input = input("Enter your name: ")
f = open("file.txt", "w")
f.write(input)
f.close()


with open("file.txt", "r") as f:
    data = f.read()
    print(data)
