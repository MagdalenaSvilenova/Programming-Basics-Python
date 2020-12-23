budget = float(input())
product = input()
counter = 0
sum = 0

while product != 'Stop':
    price = float(input())
    counter += 1
    if counter % 3 == 0:
        price /= 2

    if (sum + price) > budget:
        print("You don't have enough money!")
        print(f'You need {((price + sum) - budget):.2f} leva!')
        break
    sum += price
    product = input()

if product == 'Stop':
    print(f'You bought {counter} products for {sum:.2f} leva.')