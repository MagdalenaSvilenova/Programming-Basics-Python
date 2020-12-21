guests = int(input())
price_couvert = float(input())
budget = float(input())

cake = budget * 0.1

if 10 <= guests <= 15:
    price_couvert -= 0.15 * price_couvert
elif 15 <= guests <= 20:
    price_couvert -= 0.2 * price_couvert
elif guests > 20:
    price_couvert -= 0.25 * price_couvert

total_price = (price_couvert * guests) + cake

if budget >= total_price:
    print(f"It is party time! {(budget - total_price):.2f} leva left.")
else:
    print(f"No party! {(total_price - budget):.2f} leva needed.")