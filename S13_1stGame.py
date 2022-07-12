import random

print("The Rock, Paper, Pencil, Scissor Game")
print("By Shakil Ahmed\n\n")
print("This Game has 5 Rounds\n")
print("\t\t\t~Game Rules~")
print("The player who has the most win is the overall winner of the game.")

winner = "\n You Win !"
loser = "\nYou Lose !"
tied = "\nIt's a tie !"
com = "\nComputer's bet:"
user = "\nYou're bet"
win = 0
lose = 0
tie = 0

for i in range(1, 6):
    print(f"\nRound {i} Start!")
    listof = ["Rock", "Paper", "Pencil", "Scissor"]
    choosen = random.choice(listof)
    player = input("\n\nPlace you're bet:")

    if (player == "Rock" or player == "rock") and choosen == "Paper":
        lose = lose + 1
        print(user, player)
        print(com, choosen)
        print(loser)
    elif (player == "Rock" or player == "rock") and choosen == "Pencil":
        win = win + 1
        print(user, player)
        print(com, choosen)
        print(winner)
    elif (player == "Rock" or player == "rock") and choosen == "Scissor":
        win = win + 1
        print(user, player)
        print(com, choosen)
        print(winner)
    elif (player == "Rock" or player == "rock") and choosen == "Rock":
        tie = tie + 1
        print(user, player)
        print(com, choosen)
        print(tied)

    elif (player == "Paper" or player == "paper") and choosen == "Rock":
        win = win + 1
        print(user, player)
        print(com, choosen)
        print(winner)
    elif (player == "Paper" or player == "paper") and choosen == "Pencil":
        lose = lose + 1
        print(user, player)
        print(com, choosen)
        print(loser)
    elif (player == "Paper" or player == "paper") and choosen == "Scissor":
        lose = lose + 1
        print(user, player)
        print(com, choosen)
        print(loser)
    elif (player == "Paper" or player == "paper") and choosen == "Paper":
        tie = tie + 1
        print(user, player)
        print(com, choosen)
        print(tied)

    elif (player == "Pencil" or player == "pencil") and choosen == "Rock":
        lose = lose + 1
        print(user, player)
        print(com, choosen)
        print(loser)
    elif (player == "Pencil" or player == "pencil") and choosen == "Paper":
        win = win + 1
        print(user, player)
        print(com, choosen)
        print(winner)
    elif (player == "Pencil" or player == "pencil") and choosen == "Scissor":
        lose = lose + 1
        print(user, player)
        print(com, choosen)
        print(loser)
    elif (player == "Pencil" or player == "pencil") and choosen == "Pencil":
        tie = tie + 1
        print(user, player)
        print(com, choosen)
        print(tied)

    elif (player == "Scissor" or player == "scissor") and choosen == "Rock":
        lose = lose + 1
        print(user, player)
        print(com, choosen)
        print(loser)
    elif (player == "Scissor" or player == "scissor") and choosen == "Paper":
        win = win + 1
        print(user, player)
        print(com, choosen)
        print(winner)
    elif (player == "Scissor" or player == "scissor") and choosen == "Pencil":
        win = win + 1
        print(user, player)
        print(com, choosen)
        print(winner)
    elif (player == "Scissor" or player == "scissor") and choosen == "Scissor":
        tie = tie + 1
        print(user, player)
        print(com, choosen)
        print(tied)
    else:
        print("\nInvalid Entry")

print(f"\nYou're win: {win}")
print(f"\nYou're lose: {lose}")
print(f"\nYou're tie: {tie}")

if win == 3 and lose == 2 and tie == 0:
    print("\nCongratulations! You Win!")
elif win == 3 and lose == 1 and tie == 1:
    print("\nCongratulations! You Win!")
elif win == 3 and lose == 0 and tie == 2:
    print("\nCongratulations! You Win!")
elif win == 2 and lose == 1 and tie == 2:
    print("\nCongratulations! You Win!")
elif win == 2 and lose == 2 and tie == 1:
    print("\nSo, Close, It's a tie!")
elif win == 2 and lose == 0 and tie == 3:
    print("\nCongratulations! You Win!")
elif win == 1 and lose == 0 and tie == 4:
    print("\nCongratulations! You Win!")
elif win == 1 and lose == 1 and tie == 3:
    print("\nSo, Close, It's a tie!")
elif win == 4 and lose == 1 and tie == 0:
    print("\nCongratulations! You Win!")
elif win == 4 and lose == 0 and tie == 1:
    print("\nCongratulations! You Win!")
elif win == 5 and lose == 0 and tie == 0:
    print("\nCongratulations! You Win!")
else:
    print("\nUnfortunately! You Loser!")

    
'''Copyright © 2022 SSahmed. All rights reserved'''
