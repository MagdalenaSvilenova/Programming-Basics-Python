day = input()

ticket = 0

if day == 'Monday' or day == 'Tuesday' or day == 'Friday':
    ticket = 12
    print(ticket)
elif day == 'Wednesday' or day == 'Thursday':
    ticket = 14
    print(ticket)
elif day == 'Saturday' or day == 'Sunday':
    ticket = 16
    print(ticket)
