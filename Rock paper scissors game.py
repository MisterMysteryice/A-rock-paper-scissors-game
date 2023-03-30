import random

player_wins = 0
computer_wins = 0
draws = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type in rock/paper/scissors or q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock = 0 , paper =1 and scissors = 2

    computer_pick = options[random_number]
    print("the computer picked " + computer_pick)

    if user_input == computer_pick:
        print("Its a draw!")
        draws += 1


    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        player_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        player_wins += 1


    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        player_wins += 1

    elif user_input == "rock" and computer_pick == "paper":
        print("You lost!")
        player_wins += 1

    elif user_input == "paper" and computer_pick == "scissors":
        print("You lost!")
        player_wins += 1

    elif user_input == "scissors" and computer_pick == "rock":
        print("You lost!")
        player_wins += 1

print("You won", player_wins, "times" + " Python won", computer_wins, "times" + " and" " you drew", draws, "times"  )
print("Play again soon!")






