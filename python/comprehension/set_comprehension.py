books = [
    "The Lord of the Rings",
    "The Hobbit",
    "The Silmarillion",
    "The Hobbit",
    "The Fellowship of the Ring",
    "The Two Towers",
    "The Silmarillion",
    "The Fellowship of the Ring",
    "The Return of the King",
    "Fire and Blood",
    "The Return of the King",
    "The Children of Hurin",
    "The Return of the King",
    "The Tales of Beedle the Bard",
    "The Return of the King",
    "Fire and Blood",
]


unique_books = {book for book in books}

print(unique_books)

lenghty_names = {book for book in books if len(book) > 10}

print(lenghty_names)


ingredients = {
    "tea": ["ginger", "water", "milk"],
    "coffee": ["water", "milk", "caffine"],
    "roast": ["chile", "pepper", "salt", "chicken", "onion", "garlic"],
}


unique_indgredients = {
    spice for ingredient in ingredients.values() for spice in ingredient
}

print(unique_indgredients)
