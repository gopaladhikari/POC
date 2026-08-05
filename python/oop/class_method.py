class TeaOrder:
    def __init__(self, type_, sweet, size) -> None:
        self.type = type_
        self.sweet = sweet
        self.size = size

    @classmethod
    def from_dict(cls, dict_):
        return cls(dict_["type"], dict_["sweet"], dict_["size"])

    @classmethod
    def from_string(cls, string_):
        type_, sweet, size = string_.split(",")

        return cls(type_, sweet, size)


order1 = TeaOrder("Green", "Sweet", "Small")
order2 = TeaOrder.from_dict({"type": "Green", "sweet": "Sweet", "size": "Small"})
order3 = TeaOrder.from_string("Green,Sweet,Small")


print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)
