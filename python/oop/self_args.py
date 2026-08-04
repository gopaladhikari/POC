class TeaCup:
    size = 150

    def describe(self):
        print(f"Tea cup size is {self.size}")


cup = TeaCup()

cup.describe()


TeaCup.describe(cup)


cup_two = TeaCup()

cup_two.size = 250

TeaCup.describe(cup_two)
