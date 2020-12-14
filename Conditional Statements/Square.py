import math
figura = input()

if figura == 'square':
    side_1 = float(input())
    lice = side_1 * side_1
elif figura == 'rectangle':
    side_1 = float(input())
    side_2 = float(input())
    lice = side_1 * side_2
elif figura == 'circle':
    side_1 = float(input())
    lice = math.pi * side_1 * side_1
elif figura == 'triangle':
    side_1 = float(input())
    side_2 = float(input())
    lice = (side_2 * side_1) / 2
print(f'{lice:.3f}')
