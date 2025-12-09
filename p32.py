#recursive 

#input
def exp(number, power):
    if exp == 0:
        return 1
    elif power == 1:
        return number
    else:
        return number * power(number, power-1)




#Missing numbers
def missing(a_list):
    limit = len(array)
    freq_table = {}
    for x in array:
        freq_table[x] = 1

    for i in range(0, limit+1):
        if i not in freq_table:
            return 1
    return -1 #error code

    print(missing([3,0,1]))
    print(missing([9,6,4,2,3,5,7,0,1]))


#





