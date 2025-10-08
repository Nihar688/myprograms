#Savings Tracker

current_amount = 0

while True:
    money = int(input("How much money do you want to add to your account?: "))

    if money == 0:
        print(f"You quit! Total saved: ${current_amount}")
        break

current_amount += money 

    elif current_savings >= 100:
        print(f"Goal reached! You saved ${current_savings}")
        break

    else: 
        print(f"Current savings: ${current_savings}")

    



    