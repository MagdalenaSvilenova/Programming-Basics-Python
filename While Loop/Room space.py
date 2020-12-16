width = int(input())
length = int(input())
height = int(input())

area = width * length * height
space_needed = 0
while True:
    line = input()

    if line == 'Done':
        break
    current_box_space = int(line)
    space_needed += current_box_space

    if space_needed > area:
        break

if space_needed > area:
    print(f'No more free space! You need {space_needed - area} Cubic meters more.')
else:
    print(f'{area - space_needed} Cubic meters left.')
