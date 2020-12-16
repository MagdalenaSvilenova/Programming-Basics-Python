width = int(input())
length = int(input())
cake_size = width * length

while cake_size > 0:
    line = input()
    if line == 'STOP':
        break
    else:
        pieces = int(line)
        cake_size -= pieces

if cake_size > 0 :
    print(f"{cake_size} pieces are left." )
else:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")
