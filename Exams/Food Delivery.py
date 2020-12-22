chicken = int(input())
fish = int(input())
vegeratian = int(input())

chicken_price = 10.35
fish_price = 12.40
vegetarian_price = 8.15
delivery_price = 2.50

total_price = chicken * chicken_price + fish * fish_price + vegeratian * vegetarian_price
desert = 0.2 * total_price

total = total_price + desert + delivery_price

print(f"Total: {total:.2f}")