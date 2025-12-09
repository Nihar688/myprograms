#Longest Collatz Sequence 

def next_value(num):
    if num % 2 = 0:
        return num // 2 = 0
    else: 
        return num (3 * num) + 1 
#The iterative sequence is defined for the set of positive integers:

def sequence_maker(start, table):
    if start in table:
        return table [start]
    else: 
        sequence = [start]
        size = 1
        
