# Break =  Stops the loop

for i in range(100):
    print(i)
    if i == 50:
        break

# Continue = Skips the rest of the loop

a = 0
while a < 100:
    a += 1
    if a == 50:
        continue
    print(a)


# Pass = Skips the rest of the code


for i in range(100):
    pass
