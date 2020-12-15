budget = float(input())
seson = input()

destination = ""
vacation = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if seson == "summer":
        price = budget * 0.3
    elif seson == "winter":
        price = budget * 0.7
elif 1000 >= budget > 100:
    destination = "Balkans"
    if seson == "summer":
        price = budget * 0.4
    elif seson == "winter":
        price = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    price = budget * 0.9

if destination == "Europe":
    vacation = "Hotel"
elif seson == "summer" and not destination == "Europe":
    vacation = "Camp"
elif seson == "winter":
    vacation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{vacation} - {(price):.2f}")
