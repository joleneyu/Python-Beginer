import random

computer_choice = random.choice(["Rock, Paper, Scissors"])
user_choice = input("Do you want - Rock, Paper, or Scissors?\n")
if computer_choice == user_choice:
    print("TIE")

elif user_choice == "Paper" and computer_choice == "Rock":
    print("WIN")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("WIN")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("WIN")
else:
    print("You lose, computer wins")