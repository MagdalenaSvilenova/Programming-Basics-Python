income = float(input())
grade_avg = float(input())
income_min = float(input())

social_scholarship_1 = income_min * 0.35
grade_scholarship_1 = grade_avg * 25
social_scholarship = int(social_scholarship_1)
grade_scholarship = int(grade_scholarship_1)

if grade_scholarship >= social_scholarship:
    proverka = 1
else:
    proverka = 0

if income < income_min and grade_avg > 5.5:
    if proverka == 1:
        print(f'You get a scholarship for excellent results {grade_scholarship:.0f} BGN')
    else:
        print(f'You get a Social scholarship {social_scholarship:.0f} BGN')
elif income < income_min and grade_avg > 5.5 and social_scholarship == grade_scholarship:
    print(f'You get a scholarship for excellent results {grade_scholarship:.0f} BGN')
elif income < income_min and grade_avg > 4.5:
    print(f'You get a Social scholarship {social_scholarship:.0f} BGN')
elif grade_avg >= 5.5:
    print(f'You get a scholarship for excellent results {grade_scholarship:.0f} BGN')
else:
    print('You cannot get a scholarship!')
