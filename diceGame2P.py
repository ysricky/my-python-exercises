import random

'''
This game will play automatically between 2 players, player one and player two.
Player one and player two has numbers from shuffled dices, and then the number will be compared
to each other to decide the winner.
'''
dice = [1,2,3,4,5,6]
win_one = 0
win_two = 0

while True:
    print('----------------')
    #player one turn
    random.shuffle(dice)
    player_one = dice[0]
    print(f"Player One has {player_one}")
    
    #player two turn
    random.shuffle(dice)
    player_two = dice[0]
    print(f"Player Two has {player_two}")

    #game logic
    if player_one > player_two:
        print("Player one win!")
        win_one += 1 
    elif player_one < player_two:
        print("Player two win!")
        win_two += 1
    else:
        #the game ended when it is draw
        print("The game is draw!!!")
        #game statistics
        print(f"Player one win {win_one} times")
        print(f"Player two win {win_two} times")
        win_percentage = (win_one/(win_one+win_two))*100
        print(f"Win percentage: {round(win_percentage,2)}%")
        break