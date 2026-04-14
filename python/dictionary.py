# Dictionary = Object literal

marks = {
    "Harry": 100,
    "Ron": 100,
    "Hermione": 100,
    0: "Gopal",
    1: "Gopal",
    2: "Gopal",
}

print(type(marks))
print(marks["Harry"])


# Methods
print(marks.keys())
print(marks.values())
print(marks.items())
marks.update({"Hermione": 90, "Harry": 50, "Snape": 20})
print(marks)
print(marks.get("Hermione"))


marks["Gopal"]  # throws Error
marks.get("Gopal")  # returns None
