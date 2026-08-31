import pandas as pd

index = [1, 2, 3, 4, 5]

fruits = ["apple", "banana", "grapes", "papaya", "orange"]

pd_index = pd.Series(index)


pd_index.index = fruits


print(pd_index)

print(pd_index["banana"])

print(pd_index["apple":"papaya"])

print(pd_index.loc["grapes"])
