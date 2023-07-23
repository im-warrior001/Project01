from random import randint


# List of play options
t = ["Rock", "Paper", "Scissors"]

# Counter for the number of chances
chances = 0

# Counter for the number of wins
wins = 0

# Counter for the number of ties
ties = 0

while chances < 5:
    # Assign a random play to the computer
    computer_move = t[randint(0, 2)]

    # Get player's move
    player_move = input(
        "\nRock, Paper, Scissors? (Type 'exit' to quit The Game): ")

    # Check if player wants to exit
    if player_move.lower() == "exit":
        break

    # Check if player's move is valid
    if player_move.capitalize() not in t:
        print("Invalid input! Please enter Rock, Paper, or Scissors.")
        continue

    # Increment the number of chances
    chances += 1

    print("Player:", player_move)
    print("Computer:", computer_move)

    # Check for a tie
    if player_move.capitalize() == computer_move:
        print("It's a tie!")
        ties += 1
    # Check for winning conditions
    elif (
            (player_move.capitalize() == "Rock" and computer_move == "Scissors") or
            (player_move.capitalize() == "Paper" and computer_move == "Rock") or
            (player_move.capitalize() == "Scissors" and computer_move == "Paper")
    ):
        print("Player wins!")
        wins += 1
    # Player loses
    else:
        print("Computer wins!")

# Print the final results
print("\nGame Over!")
print("Wins:", wins)
print("Ties:", ties)
print("Losses:", chances - wins - ties)
