budget = float(input())
people_count = int(input())
clothing_price = float(input())

decor = 0.1 * budget
total_clothing_count = clothing_price * people_count

if people_count > 150:
    total_clothing_count = total_clothing_count - total_clothing_count * 0.1

money_needed = decor + total_clothing_count

if money_needed <= budget:
    print('Action!')
    print(f'Wingard starts filming with {(budget - money_needed):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {(money_needed - budget):.2f} leva more.')
