prices = [50, 150, 30, 200, 90]
new_prices = []

for price in prices:
    if price < 100:
        new_price = price * 1.1  # увеличение на 10%
    else:
        new_price = price * 1.05  # увеличение на 5%
    new_prices.append(new_price)

print(new_prices)
