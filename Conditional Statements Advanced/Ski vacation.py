days = int(input())
apartment = input()
grade = input()

nights = days - 1
price = 0

if apartment == 'room for one person':
    price += 18 * nights
elif apartment == 'apartment':
    price += 25 * nights
    if nights < 10:
        price = price - (price * 0.3)
    elif 10 <= nights <= 15:
        price = price - (price * 0.35)
    else:
        price = price - (price * 0.5)
elif apartment == 'president apartment':
    price += 35 * nights
    if nights < 10:
        price = price - (price * 0.1)
    elif 10 <= nights <= 15:
        price = price - (price * 0.15)
    else:
        price = price - (price * 0.2)

if grade == 'positive':
    price += price * 0.25
elif grade == 'negative':
    price -= price * 0.10

print(f'{price:.2f}')
