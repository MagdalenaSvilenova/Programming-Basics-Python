days = int(input())
bakers_count = int(input())
cake = int(input())
gofr = int(input())
panecake = int(input())

sum_cake = cake * 45
sum_gofr = gofr * 5.8
sum_panecake = panecake * 3.2

sum = days * bakers_count * (sum_cake + sum_gofr + sum_panecake)
total = sum - sum / 8
print(total)
