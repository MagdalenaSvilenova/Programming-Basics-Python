import math
record = float(input())
distance = float(input())
minutes_time = float(input())

time = distance * minutes_time
naklon = math.floor(distance / 50) * 30
total_time = time + naklon

if total_time < record:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {abs(record - total_time):.2f} seconds slower.")