#String Checklist 

#1. Create an empty string 
empty_string = ""
ver2 = ''
#2. Determine if a string is empty 
# method 1: 
if not str_var:
    print("str_var is empty!")
if len(str_var) == 0
    print("str_var is empty!")
#3. Format a string to contain dynamic data 
name = "Huzztin"
str_var = f"Hello {name}!"
#4. Access individual characters/items in a string
print(name[0])
print(name[-2])
#5. Access the first, access the last item in a string 
print(name[0]) #zero index is always the first 
print(name[len(name)-1]) #this gives last 
print(name[-1]) #this alsp gives last 
#6. Join two/multiple strings together 
a = "poo"
b = "poo"
c = a + b 
print(c) #we expect poopoo 
#7. Reverse a string
temp = "park"
reversed_temp = temp[::-1]
v2 = ''.join(reversed(temp)) 
#8. Create a copy of a string 
temp = "hydroflask" 
temp_copy = temp[:]
another_copy = temp
#9. Compare strings for equality 
a = "marshall"
b = "dog"
status = a == b
#10. Determine the minimum and maxiumum values within a string 
