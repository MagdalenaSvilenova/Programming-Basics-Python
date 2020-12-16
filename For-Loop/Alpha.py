text = input()
total = 0

for index in range(0, len(text)):
    symbol = text[index]

    if symbol == 'a' or symbol == 'A':
        total += 1
    elif symbol == 'e' or symbol == 'E':
        total += 2
    elif symbol == 'i' or symbol == 'I':
        total += 3
    elif symbol == 'o' or symbol == 'O':
        total += 4
    elif symbol == 'u' or symbol == 'U':
        total += 5

print(total)
