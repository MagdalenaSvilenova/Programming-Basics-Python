steps = 0
steps_home = 0

while steps < 10000:
    line = input()
    if line == 'Going home':
        steps_home = int(input())
        steps += steps_home
        break
    else:
        steps += int(line)

if steps >= 10000:
    print('Goal reached! Good job!')
    print(f"{steps - 10000} steps over the goal!")
else:
