max_hours = 24
max_minutes = 60

for hour in range (0, max_hours):
    hour_str = hour
    if hour < 10:
        hour_str = '0' + str(hour)
    for minute in range (0, max_minutes):
        minutes_str = minute
        if minute < 10:
            minutes_str = '0' + str(minute)
        print(f'{hour}:{minute}')
