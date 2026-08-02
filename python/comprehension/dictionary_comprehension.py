tea_price_npr = {"Green": 15, "Black": 15, "Oolong": 20, "milk": 20}

tea_price_usd = {
    tea: (price / 152).__round__(2) for tea, price in tea_price_npr.items()
}

print(tea_price_usd)
