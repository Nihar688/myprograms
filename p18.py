#1. Create an empty list
a_list = []
b_list = list() #another way
#2. Determine if a string is empty
if not a_list:
    print("a_list is empty!")
if len(a_list_) == 0:
    print("a_list is empty!")
#3. What does len(), sum(), min(), max() do when a list is an argument?
c_list = [3,1,4,1,5,9]
print(len(c_list)) #expect 6 
print(sum(c_list)) #23 
print(min(c_list))
print(max(c_list))
#4. Access individual characters/items in a list
d_list = list("hello, world!")
print(d_list[0])#"h"
print(d_list(-1))#"!"
print(d_list[1:4])# ["e", "l", "l"]
#5. Access the first, access the last item in a list
#6. Join two/multiple lists together
a = [3,1,4]
b = ["Marshall","Freya","Joy"]
c = a + b #Creates a new list of a and b joined 
a.extend(b) #this mutates a to give the contents of b 
a = [3,1,4]
for item in b:
    a. append(item
#7. Reverse a list (two ways)
#8. Create a copy of a list (two ways)
#9. Compare lists for equality
#10. Determine if an item within a list
#11. Locate the index of a item exists within a list
#12. Count how often an item occurs within a list
#13. Convert a string to a list
#14. Sort a list
#15. Sort two lists where the index are attached to each other based on one of the lists 



#Ex. 
    #fruits = ['apple', 'blueberry', 'cantaloupe']
    #inventory = [12, 4, 67]

    #result 
    #fruits ['blueberrt', 'apple', 'cantaloupe']
    #inventory = [4, 12, 67]