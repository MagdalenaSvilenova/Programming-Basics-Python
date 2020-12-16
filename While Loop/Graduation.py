name = input()
year = 1
isFlanked = False
grades_sum = 0

while year <= 12:
    current_grade = float(input())
    if current_grade < 4:
        if isFlanked:
            break
        isFlanked = True
        continue
    grades_sum += current_grade
    year += 1
if year <= 12:
    print(f'{name} has been excluded at {year} grade')
else:
    print(f'{name} graduated. Average grade: {grades_sum / 12:.2f}')
