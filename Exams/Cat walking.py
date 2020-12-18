min_walking = int(input())
counter = int(input())
calories = int(input())

burned_calories = min_walking * 5 * counter
if burned_calories >= calories / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")