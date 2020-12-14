dep_sum = float(input())
dep_months = int(input())
air = float(input())

sum = dep_sum + dep_months * ((dep_sum * (air / 100) ) / 12)
print(sum)
