#chores

#define variables - 

Time = int(input())
#read total minutes available 

Chores = int(input())
#Read the number the chores to do

#Read each chore time to a list
chores = [] #empty list 
for i in range(Chores):
    chores.append(int(input()))
    #move into the list

#sort chores from smallest time to the largest
chores.sort()

#count how many chores we can complete
time_used = 0
count = 0

for t in chores:
    if time_used + Time <= t:
        time_used += t 
        count += 1
    else:
        break

print(count)




#setup 
time_left = int(input()) #for time alloted
chores = int(input()) #how many chores
time per chore = []
for i in range(chores):
    time_per_chore.append(int(input())) #inputting each chore's duration

#Step 1 --> sort chores from least to greatest
time_per_chore.sort()

while time left > 0 and time_per_chore:
    time_left == time_per_chore[0]
    chore_ctr += 1
    time_per_chore.pop(0) 