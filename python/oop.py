class Employee:
    language = "Python"
    salary = 1000


harry = Employee()
print(harry.language)
print(harry.salary)

# self parameter


class Animal:
    legs = 4
    sound = "bark"

    def getDetails(self):
        return f"Legs: {self.legs}, Sound: {self.sound}"

    @staticmethod
    def greet():
        print("Hello world")


dog = Animal()
print(dog.getDetails())  # Animal.getDetails(dog)


class Car:
    def __init__(self, name, cost, color):
        self.name = name
        self.cost = cost
        self.color = color
        print("I am creating an object.")


tesla = Car("Tesla", 12000, "Red")

print(tesla.name)
print(tesla.cost)
print(tesla.color)
