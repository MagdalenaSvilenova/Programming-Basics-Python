first_player = input()
second_player = input()
card1 = input()
points1 = 0
points2 = 0

while card1 != 'End of game':
    card2 = int(input())
    card11 = int(card1)
    if card11 > card2:
        points1 += card11 - card2
    elif card2 > card11:
        points2 += card2 - card11
    else:
        print(f"Number wars!")
        last_card1 = int(input())
        last_card2 = int(input())
        if last_card1 > last_card2:
            print(f"{first_player} is winner with {points1} points")
            break
        else:
            print(f"{second_player} is winner with {points2} points")
            break
    card1 = input()

if card1 == 'End of game':
    print(f"{first_player} has {points1} points")
    print(f"{second_player} has {points2} points")