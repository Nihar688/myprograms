#Non-destruvtive selection sort with lists 

def select(a_list): 
    if len(a_list) <= 1:
        return a_list 
    else:
        i = 0 #to look at individual values 
        while i < len(a_list):
            smallest = a_list[i] #then prove it is or not 
            j = i + 1 #
            new_location = i #initialize to 1
            while j < len(a_list):
                new_value = a_list[j]
                if new_value < smallest:
                    smallest = new_value 
                    new_location = j
                j += 1 
            #swap the smallest into the proper location 
            temporary = a_list[1]
            a_list[i] = smallest
            a_list[new_location] = temporary
            #python way
            #a_list[i], a_list[new_location] = a_list[new_location], a_list[i]
            i += 1 

