#Computer Guessing Game

import random 

roll = random.randint(1, 50)

while True:
    Guess = int(input("Pick a number between 1 and 50: "))

    if Guess > roll:
        print("Too High!")

    elif Guess < roll:
        print("Too Low")

    else:
        print("You got it!")
        break




