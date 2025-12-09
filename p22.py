def eve_odd(a_list):
    even = []
    odd = []
    for val in a_list : 
        if val % 2 == 0:
            even.append(val)
        else:
            odd.append(val)
        #end of for 
        if len (even) > len(odd):
            return even
        elif len(odd) > len(even):
            return odd
        else: 
            return []






#problem 2
def sel_sort(a_list):
    result = []
    while len(a_list) > 0:
        val = max(a_list)
        result.append(val)
        a_list.remove (val)
    return result 

def bubble(a_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(a_list))
        if a_list[i] > a_list[i-1]
            a list [i-1], a_list[i]
        swapped = True
    return a_list
