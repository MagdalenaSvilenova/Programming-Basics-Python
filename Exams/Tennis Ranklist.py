import math
games = int(input())
start_points = int(input())
counter_w = 0
final_points = 0

for game in range(1, games + 1):
    result = input()
    if result == 'W':
        final_points += 2000
        counter_w += 1
    elif result == 'F':
        final_points += 1200
    elif result == 'SF':
        final_points += 720

points_avg = final_points / games
p = (counter_w / games) * 100

print(f"Final points: {(final_points+start_points)}")
print(f"Average points: {math.floor(points_avg)}")
print(f"{p:.2f}%")