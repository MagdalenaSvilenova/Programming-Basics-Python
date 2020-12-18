fruit = input()
pack = input()
pack_amount = int(input())
price = 0

if fruit == 'Watermelon':
    if pack == 'small':
        price = 2 * 56 * pack_amount
    else:
        price = 5 * 28.70 * pack_amount
elif fruit == 'Mango':
    if pack == 'small':
        price = 2 * 36.66 * pack_amount
    else:
        price = 5 * 19.60 * pack_amount
elif fruit == 'Pineapple':
    if pack == 'small':
        price = 2 * 42.10 * pack_amount
    else:
        price = 5 * 24.80 * pack_amount
elif fruit == 'Raspberry':
    if pack == 'small':
        price = 2 * 20 * pack_amount
    else:
        price = 5 * 15.20 * pack_amount


if 400 <= price <= 1000:
    price -= 0.15 * price
elif price > 400:
    price -= 0.5 * price

print(f"{price:.2f} lv.")