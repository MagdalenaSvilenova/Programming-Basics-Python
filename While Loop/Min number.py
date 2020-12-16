min_number = int(input())
line = input()

while not line == 'Stop':
    current_number = int(line)
    if current_number < min_number:
        min_number = current_number
    line = input()
print(min_number)
