import sys
n = int(input())
max_number = -sys.maxsize
sum = 0

for index in range(1, n + 1):
    number = int(input())
    if max_number < number:
        max_number = number
    sum += number

sum -= max_number
if sum == max_number:
    print('Yes')
    print(f'Sum = {sum}')
else:
    print('No')
    print(f'Diff = {abs(sum - max_number)}')
