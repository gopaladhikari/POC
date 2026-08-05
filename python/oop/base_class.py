class Tea:
    def __init__(self, type_, strength) -> None:
        self.type = type_
        self.strength = strength


# Code Duplication Way
class GingerTea(Tea):
    def __init__(self, type_, strength, spice_level) -> None:
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level


# Explicit Way
class LemonTea(Tea):
    def __init__(self, type_, strength, spice_level) -> None:
        Tea.__init__(self, type_, strength)
        self.spice_level = spice_level


# super() way
class GreenTea(Tea):
    def __init__(self, type_, strength, spice_level) -> None:
        super().__init__(type_, strength)
        self.spice_level = spice_level
