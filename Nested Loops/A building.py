floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    room_type = ''
    if floor == floors:
        room_type = "L"
    elif floor % 2 == 1:
        room_type = 'A'
    else:
        room_type = 'O'
    for room in range(0, rooms):
        print(f'{room_type}{floor}{room}', end=' ')
    print()
