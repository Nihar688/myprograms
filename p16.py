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
temp = "hydroflask"
print(max(temp))
print(min(temo))
print(max('hello', 'goodbye'))
print(min('1','2','3','!'))
#11. Determine if an item or a pattern exists with a string 
word = "poopooplatter"
if "poo" in word:
    print("There is poo!")
#12. Locate the index of a item or a pattern within a string 
poop_location = word.find("poo")
poop_location = word.index("poop")
#13. Count how often an item or a pattern occurs within a string
poop_count = word.count("poo")
#14. Convert all items in a string to uppercase/lowercase
yell_hydroflask = "hydroflaks".upper()
calm_hydroflask = yell_hydroflask.lower()
#15. Determine if the string can be converted to an integer
#16. Convert a string to an integer 
str_num = "67"
num = 0
if str_num.isdigit():
    num = int(str_num)
#17. Determine if a string only contains alphabetical characters
word = "shsm".isalpha()
#18. Remove non-aplhabetical characters from a string, sometimes...it is easier to create/grow than remove
gibberish = "!y87y382iwuherj@@#*#*#&"
clean = ""
i = 0 
while i < len(gibberish):
    if gibberish[i].isalpha():
        clean += gibberish[i]
    i += 1 
#19. Remove all alphabetical characters from a string 
gibberish = "!y87y382iwuherj@@#*#*#&"
clean = ""
i = 0 
while i < len(gibberish):
    # if not gibberish[i].isalpha():
    if gibberish[i].isalpha() == False:
        clean += gibberish[i]
    i += 1 
#20. Remove all whitespace from a string 
example = "h h h h h h h h h h h e l l               l o"
example = example.replace(" ", "")
#21. Sort a string in ASCII order or reverse-ASCII order
