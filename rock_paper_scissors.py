import random

user_wins = 0
comp_wins = 0

options = ["Rock", "Paper", "Scissors", "Q"]

while True:
    print("โจWelcome to the game of Rock, Paper, Scissors!!โจ")
    user_input = input("Please choose Rock/Paper/Scissors or Q to quit: ")

    if user_input == "Q":
        break

    if user_input not in options:
        user_input = input("Please choose Rock/Paper/Scissors or Q to quit: ")

    random_no = random.randint(0,2)
    comp_pick = options[random_no]
    print("Computer picked " + comp_pick + ".")

    if user_input == "Rock" and comp_pick ==  "Scissors":
        print("You Win!!๐๐")
        user_wins += 1

    elif user_input == "Paper" and comp_pick ==  "Rock":
        print("You Win!!๐๐")
        user_wins += 1

    elif user_input == "Scissors" and comp_pick ==  "Paper":
        print("You Win!!๐๐")
        user_wins += 1

    elif user_input == "Rock" and comp_pick ==  "Rock":
        print("It's a Draw๐")

    elif user_input == "Paper" and comp_pick ==  "Paper":
        print("It's a Draw๐")

    elif user_input == "Scissors" and comp_pick ==  "Scissors":
        print("It's a Draw๐")

    else:
        print("You Lost๐ฅ, Better luck next time๐")
        comp_wins += 1

print("You won", user_wins, "times.")
print("Computer won", comp_wins, "times.")
print("Goodbye, have a nice day๐")



