import math
record = float(input())
distance = float(input())
time = float(input())

ivan = time * distance
delay = int((distance / 15)) * 12.5
total_time = ivan + delay
nedostig = total_time - record
math.floor(nedostig)
if record > total_time:
    print(f'Yes, he succeeded! The new world record is {(total_time):.2f} seconds.')
else:
    print(f'No, he failed! He was {(nedostig):.2f} seconds slower.')
