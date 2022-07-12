#Guessing Game
from random import randint
randVal = randint(0, 100)


while True:
    guess = int(input("Enter a random Number between 0 and 100\n"))
    if guess == randVal:
        break
    elif guess < randVal:
        print("Your guess too low!")
    else:
        print("Your guess too high! ")
print("Your guess is correct")

'''Copyright © 2022 SSahmed. All rights reserved'''
