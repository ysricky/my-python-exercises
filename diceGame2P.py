import random

dice = [1,2,3,4,5,6]
win_one = 0
win_two = 0

while True:
    print('----------------')
    random.shuffle(dice)
    player_one = dice[0]
    print(f"Player 1 has {player_one}")
    random.shuffle(dice)
    player_two = dice[0]
    print(f"Player 2 has {player_two}")
    if player_one > player_two:
        print("Player one win!")
        win_one += 1 
    elif player_one < player_two:
        print("Player two win!")
        win_two += 1
    else:
        print("The game is draw!!!")
        print(f"Player one win {win_one} times")
        print(f"Player two win {win_two} times")
        win_percentage = (win_one/(win_one+win_two))*100
        print(f"Win percentage: {win_percentage}%")
        break