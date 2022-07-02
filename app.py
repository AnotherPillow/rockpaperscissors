import random
import os
from won import winner
from logo import logo

def main():
    print("What is your move?: "); player_guess = input()

    if player_guess == "rock":
        player_guess = "rock"
    elif player_guess == "paper":
        player_guess = "paper"
    elif player_guess == "scissors":
        player_guess = "scissors"

    computer_guess = random.choice(["rock", "paper", "scissors"])

    print(winner(player_guess,computer_guess))
    print("Would you like to play again? (y/n)")
    if input() == "y":
        main()
    else:
        print("Thanks for playing!")
        os.system("clear")
        print(logo())
        exit()

if __name__ == "__main__":
    print(logo())
    main()