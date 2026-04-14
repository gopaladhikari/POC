f = open("python/file.txt")

data = f.read()

print(data)

f.close()

input = input("Enter your name: ")
f = open("python/file.txt", "w")
f.write(input)
f.close()
