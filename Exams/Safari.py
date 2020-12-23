budget = float(input())
fuel_liters = float(input())
day = input()

fuel = 2.10
guide = 100
money_needed = fuel_liters * fuel + guide

if day == 'Saturday':
    money_needed -= money_needed * 0.1
else:
    money_needed -= money_needed * 0.2

if budget > money_needed:
    print(f'Safari time! Money left: {(budget - money_needed):.2f} lv.')
else:
    print(f'Not enough money! Money needed: {(money_needed - budget):.2f} lv.')