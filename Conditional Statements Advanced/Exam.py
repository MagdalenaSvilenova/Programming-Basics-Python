exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour *60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes

time_difference = arrival_time - exam_time
my_time = ""

if time_difference < -30:
    my_time = "Early"
elif time_difference <= 0:
    my_time = "On time"
else:
    my_time = "Late"

result = ""
if time_difference != 0:
    hours = abs(time_difference) // 60
    minutes = abs(time_difference) % 60
    if hours > 0:
        if time_difference < 0:
            result = f'{hours}:{minutes:02d} hours before the start'
        else:
            result = f'{hours}:{minutes:02d} hours after the start'
    else:
        if time_difference < 0:
            result = f'{minutes} minutes before the start'
        else:
            result = f'{minutes} minutes after the start'

print(f'{my_time}')
if time_difference != 0:
    print(f'{result}')
