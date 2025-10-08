#Dice Roller Game 

#player starts = 0 points 
import random 

current_points = 0 

while True: 
    Dice = (input("Do you want to roll the dice? (yes or no): "))

    if Dice == "no":
        print("You Quit")
        break

    elif Dice == "yes":
        roll = random.randint(1, 6)
        current_points += roll
        print(f"You rolled a {roll}! Total points; {current_points}")
        
        if current_points >= 20:
            print("You win!")
            break

    else : 
        print ("Please type 'yes' or 'no'.")







