def bubble(a_list): 
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(a_list)):
            if a_list[i-1] > a_list[i]:
                swapped = True
                a_list[i-1], a_list[i] = a_list[i], a_list[i-1]
        #end of inner for
    #end of outer while
    return a_list





























def inserty(a_list):
    i = 1
    while i < len(a_list):
        j = 1 
        while j > 0:
            if a_list[j-1] > a_list[j]:
                a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
            else:
                break 
            j -= 1 #j = j-1 
        i += 1

        

















#CHALLENGE 
def sort_it(a_list, b_list):
    #a_list[0] -> b_list[0]
        #order          #connected 
    #equal length 


