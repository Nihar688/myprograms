#Heads and Tails Game 

from random import choice # learing one thing rather than "importing math", function that randomly chooses from a list - choice
while True: 
    print ("Welcome to our heads and talks game!")
    print("Please chose either heads or tails")
    while True: 
        user_input = input ("User's choice: ")
        user_input = user_input.lower() #makes things lowercased 

        if user_input in {"heads", "tails", "head", "tail"}:
            #user_input was valid, we can exit the infinite loop, valid input 
            break #exits the looping strucuture "intended to avoid inapporpriate answers"
        else: 
            print("pleas type in heads or tails. :)")
    #end of while 
    flip_result = choice(["heads", "tails"])
    print(f"The computer flipped: {flip_result}")
    if user_input in {"heads", "head"} and flip_result == "heads":
        print ("You guessed right!")
    elif user_input in {"tails", "tail"} and flip_result == "tails":
        print ("You guessed right!")
    else: 
        print ("you're wrong fatass")
        
    user_input = input("Want to exit?: Yes/No. ")
    if user_input.lower() == "yes":
        break

    elif user_input.lower() == "no":
        continue



#18 line - condition from user_input to the end of the head bracket + Logical end + condition flip_result = "heads"
    #Conditions created by comparative code 
#probabilty??????? 
# % ????
#if statement ?????
