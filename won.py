def winner(player_guess,computer_guess):
    if player_guess == computer_guess:
        return "It's a tie!"
    elif player_guess == "rock":
        if computer_guess == "paper":
            return "You lose!"
        else:
            return "You win!"
    elif player_guess == "paper":
        if computer_guess == "scissors":
            return "You lose!"
        else:
            return "You win!"
    elif player_guess == "scissors":
        if computer_guess == "rock":
            return "You lose!"
        else:
            return "You win!"
    else:
        return "You didn't pick rock, paper, or scissors. Try again."
    