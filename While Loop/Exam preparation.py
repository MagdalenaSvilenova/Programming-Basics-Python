threshold = int(input())
times = 0
problems_count = 0
grades_sum = 0
last_problem = ''
has_failed = True

while times < threshold:
    problem_name = input()
    if problem_name == 'Enough':
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        times += 1
    grades_sum += grade
    problems_count += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {threshold} poor grades.")
else:
    print(f"Average score: {grades_sum / problems_count:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {last_problem}")
