donuts = int(input("Enter the number of donuts: "))
events = int(input("Enter the number of events: "))
#stop when no donut or event 
current_event = 1 
while current_event <= events and donuts >= 0: 
    event_type = input("+ or - ?: ")
    donuts_amount = int(input("Enter donut amount: "))
    if event_type == "+":
        donuts = donuts + donuts_amount
        #donut_count += donut_amount 
    elif event_type == "-":
        donuts = donuts - donuts_amount 
    else:
        print("shutup")
    current_event = current_event + 1
#end of while
print(f"At the end of our events, we have {donuts} donuts. ")
