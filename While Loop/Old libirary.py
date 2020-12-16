count = 0
book = input()

while True:
    current_book = input()
    if current_book == book:
        print(f'You checked {count} books and found it.')
        break
    if current_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {count} books.')
        break
    count += 1
