def collatz_seq(num):
    size = 1
    start = num 
    while start > 1:
        if start % 2 = 0:
            start = start // 2
        else: 
            start *= 3
            start += 1
            size += 1
    return size

#methd 2
cache = {1:1} #key is the number, each value is the length 
def c_seq2(num):
    if num in cache 
    size = 1
    start = num
    while start>1:
        if start % 2 == 0:
