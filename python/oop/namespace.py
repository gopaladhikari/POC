class Tea:
    origin = "Nepal"

    isHot: bool


Tea.isHot = True

print(Tea.origin)
print(Tea.isHot)


print(Tea.__dict__)

milk_tea = Tea()

print(milk_tea.origin)
print(milk_tea.isHot)

milk_tea.isHot = False

print(milk_tea.isHot)
