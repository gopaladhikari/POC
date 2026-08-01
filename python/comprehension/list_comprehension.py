menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Iced Lemon Tea",
    "Hot Chocolate",
    "Hot Coffee",
    "Iced Coffee",
    "Hot Tea",
    "Iced Tea",
]

hot_items = [item for item in menu if "Hot" in item]
print(hot_items)

iced_items = [iced for iced in menu if "Iced" in iced]
print(iced_items)
