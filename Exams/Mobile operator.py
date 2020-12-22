srok_dogovor = input()
tip_dogovor = input()
mob_net = input()
months = int(input())
price = 0

if srok_dogovor == 'one':
    if tip_dogovor == 'Small':
        price = 9.98
    elif tip_dogovor == 'Middle':
        price = 18.99
    elif tip_dogovor == 'Large':
        price = 25.98
    elif tip_dogovor == 'ExtraLarge':
        price = 35.99
elif srok_dogovor == 'two':
    if tip_dogovor == 'Small':
        price = 8.58
    elif tip_dogovor == 'Middle':
        price = 17.09
    elif tip_dogovor == 'Large':
        price = 23.59
    elif tip_dogovor == 'ExtraLarge':
        price = 31.79

if mob_net == 'yes':
    if price <= 10.00:
        price += 5.50
    elif price <= 30.00:
        price += 4.35
    elif price > 30.00:
        price += 3.85

total = price * months
if srok_dogovor == 'two':
    total -= total * 0.0375

print(f'{total:.2f} lv.')