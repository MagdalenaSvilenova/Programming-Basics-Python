bitcoin = int(input())
chinees = float(input())
commition = float(input())

sum_bitcoini = bitcoin * 1168
sum_chines = (chinees * 0.15) * 1.76
total = (sum_bitcoini + sum_chines) / 1.95

sum_komisionna = (commition * total) / 100
final = total - sum_komisionna
print(f'{final:.2f}')