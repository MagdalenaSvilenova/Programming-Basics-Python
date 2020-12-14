puzzle = 2.60
doll = 3
bear = 4.10
minion = 8.20
truck = 2
trip_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

income = puzzle * puzzle_count + doll * doll_count + bear * bear_count + minion * minion_count + truck * truck_count
total_toys = puzzle_count + doll_count + bear_count + minion_count + truck_count

if total_toys >= 50:
    income -= income * 0.25

income -= income * 0.1

if income >= trip_price:
    print(f'Yes! {income - trip_price:.2f} lv left.')
else:
    print(f'Not enough money! {trip_price - income:.2f} lv needed.')
