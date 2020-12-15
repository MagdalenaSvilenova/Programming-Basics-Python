num_1 = int(input())
number_2 = int(input())
op = input()
result = 0
state = ""

if op == "+":
    result = num_1 + number_2
    if result % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num_1} {op} {number_2} = {result} - {state}")
elif op == "-":
    result = num_1 - number_2
    if result % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num_1} {op} {number_2} = {result} - {state}")
elif op == "*":
    result = num_1 * number_2
    if result % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num_1} {op} {number_2} = {result} - {state}")
elif op == "/":
    if number_2 == 0:
        print(f"Cannot divide {num_1} by zero")
    else:
        result = num_1 / number_2
        print(f"{num_1} / {number_2} = {(result):.2f}")
elif op == "%":
    if number_2 == 0:
        print(f"Cannot divide {num_1} by zero")
    else:
        result = num_1 % number_2
        print(f"{num_1} % {number_2} = {result}")
