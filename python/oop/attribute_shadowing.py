class Tea:
    temperature = "Hot"
    strength = "Medium"
    size: str


cutting = Tea()


print(cutting.temperature)
print(cutting.strength)

cutting.temperature = "Cold"
cutting.size = "Small"

print(cutting.temperature)
print(cutting.strength)
print(cutting.size)  # AttributeError and this is attribute shadowing


del cutting.temperature
del cutting.size

print(cutting.temperature)
print(cutting.size)


"""
If you lost the reference of a attribute from a object, it will fallback the the class attribute
"""
