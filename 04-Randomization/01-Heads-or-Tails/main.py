import random

User_choice= input("Choose the toss. Type Heads or Tails: ").title()
computer_choice= random.choice(["Heads", "Tails"])

if User_choice == computer_choice:
    print("You win!")
else:
    print("you lost!")
