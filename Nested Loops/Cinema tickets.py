standard = 0
student = 0
kid = 0

movie_name = input()
while movie_name != 'Finish':
    empty_spaces = int(input())
    tickets = 0

    ticket_type = input()
    while ticket_type != 'End':
        if ticket_type == 'standard':
            standard += 1
        elif ticket_type == 'student':
            student += 1
        else:
            kid += 1
        tickets += 1

        if tickets == empty_spaces:
            break
        ticket_type = input()

    percentage_full = tickets / empty_spaces * 100
    print(f'{movie_name} - {percentage_full:.2f}% full.')

    movie_name = input()

total_tickets = kid + student + standard
print(f'Total tickets: {total_tickets}')
print(f'{student / total_tickets * 100:.2f}% student tickets.')
print(f'{standard / total_tickets * 100:.2f}% standard tickets.')
print(f'{kid / total_tickets * 100:.2f}% kids tickets.')
