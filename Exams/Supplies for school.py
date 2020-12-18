himikali = int(input())
markeri = int(input())
preparat = float(input())
namalenie = int(input())

price_himikali = himikali * 5.8
price_markeri = markeri * 7.2
price_preparat = preparat * 1.2

money_needed = price_himikali + price_markeri + price_preparat
otstupka = (money_needed * namalenie) / 100

final = money_needed - otstupka
print(f'{final:.3f}')