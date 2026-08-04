class Tea:
    def __init__(self, type_, size) -> None:
        self.type = type_
        self.size = size

    def summary(self):
        print(f"Tea type is {self.type} and size is {self.size}")


first_order = Tea("Milk", "Small")
first_order.summary()
