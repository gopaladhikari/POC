"""
1 for snake, 2 for water, 3 for gun
"""

import random


computer = random.choice([1, 2, 3])
you = input("Enter your choice, s, w, g: ")
yourDic = {
    "s": 1,
    "w": 2,
    "g": 3,
}
youVal = yourDic[you]


if youVal == computer:
    print("Tie")
elif youVal > computer:
    print("You win")
else:
    print("Computer win")
