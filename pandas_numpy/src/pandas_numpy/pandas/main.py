import pandas as pd

s = pd.Series(
    [
        1,
        2,
        3,
        45,
        50,
        44,
        52,
        645,
        5,
        4,
        55,
        5,
        444,
        2152,
        45,
        45,
        45,
        45,
        45,
        45,
        451,
        2514,
        454,
        54,
        5,
        145,
        145,
        45,
        12,
        1,
        215745,
        12,
        125,
        485,
        465,
        4654,
        54,
        54,
        245,
        432,
        16514,
        254,
        544,
        34,
        544,
        54,
        4544,
        54,
        4,
    ]
)


s.name = "numbers"


def main():
    print(s)
    print(s.dtype)
    print(s.values)
    print(s.name)
    print(s.iloc[3])
    print(s.iloc[[3, 13, 4]])  # type: ignore
