class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def show(self):
        print(f"Name is {self.name} and salary is {self.salary}")


class Programmer(Employee):
    company = "Microsoft"

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def showlanguage(self):
        print(f"Programming language is {self.language}")


gopal = Employee("Gopal", 1000)

adhikari = Programmer("Adhikari", 1000, "Python")

gopal.show()
adhikari.show()
adhikari.showlanguage()
