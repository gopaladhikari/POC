class BaseTea:
    def __init__(self, type_) -> None:
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} tea")


class MasalaTea(BaseTea):
    def add_spices(self):
        print("Adding masala spices")


class TeaShop:
    tea_cls = BaseTea  # Composition

    def __init__(self) -> None:
        self.tea = self.tea_cls("Masala")

    def serve(self):
        print(f"serving {self.tea.type} tea")
        self.tea.prepare()


class FancyShop(TeaShop):
    tea_cls = MasalaTea


shop = TeaShop()
shop.serve()

fancy_shop = FancyShop()
fancy_shop.serve()
fancy_shop.tea.add_spices()
