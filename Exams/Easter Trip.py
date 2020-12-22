destination = input()
data = input()
nights = int(input())
price = 0

if destination == 'France':
    if data == '21-23':
        price = 30
    elif data == '24-27':
        price = 35
    elif data == '28-31':
        price = 40
elif destination == 'Italy':
    if data == '21-23':
        price = 28
    elif data == '24-27':
        price = 32
    elif data == '28-31':
        price = 39
elif destination == 'Germany':
    if data == '21-23':
        price = 32
    elif data == '24-27':
        price = 37
    elif data == '28-31':
        price = 43
        
total_price = price * nights
print(f"Easter trip to {destination} : {total_price:.2f} leva.")