couzunaci = int(input())
chef_name = ' '
grade = 0
second_grade = ' '
points = 0
current_result = 0
chef_counter = 0
current_chef= ' '

for every in range(1, couzunaci + 1):
    chef_name = input()
    chef_counter += 1
    while second_grade != 'Stop':
        grade = input()
        if grade == 'Stop':
            break
        else:
            grade_1 = int(grade)
            points += grade_1
            second_grade = str(grade_1)
    if points > current_result:
        print(f'{chef_name} has {points} points.')
        print(f'{chef_name} is the new number 1!')
        current_result = points
        current_chef = chef_name
        points = 0
    else:
        print(f'{chef_name} has {points} points.')
        points = 0

print(f'{current_chef} won competition with {current_result} points!')