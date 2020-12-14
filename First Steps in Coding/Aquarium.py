length = int(input())
width = int(input())
heigth = int(input())
pzo = float(input())

volume = (length * width * heigth) * 0.001
percentage = pzo * 0.01
total = volume * (1 - percentage)
print(total)
