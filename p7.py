#Perfect Number
def is_perfect(num):
    divider = 1
    total = 0
    while divider < num:
        if num % divider == 0:
            total += divider # otal = total + divider
        divider += 1
    return total == num 
#end of is_perfect()
number = 1
while number <= 1000000:
    if is_perfect(number):
    #if is_perfect(number) == True:
        print (f"{number} is pefect.")
    number += 1
