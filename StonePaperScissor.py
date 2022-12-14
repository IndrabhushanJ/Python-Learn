import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissors?: ").lower()

    if computer == player:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("Computer: ", computer)
        print("Player: ", player)
        print("You won!! 🎉")
    elif player == "paper" and computer == "rock":
        print("Computer: ", computer)
        print("Player: ", player)
        print("You won!! 🎉")
    elif player == "scissors" and computer == "paper":
        print("Computer: ", computer)
        print("Player: ", player)
        print("You won!! 🎉")
    else:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Computer💻 won!!")

    play_again = input("Play Again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!👋🏼")
