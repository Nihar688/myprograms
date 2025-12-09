def median(a_list):
    i = 0 
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(a_list)):
            if a_list[i] < a_list[i-1]:
                a_list[i-1], a_list[i] = a_list[i], a_list[i-1]
                swapped = True
    n = len(a_list)
    if n % 2 == 1: 
        median = a_list[int(n // 2)]
        return median
    else:
        middle1 = a_list[int(n / 2) - 1]
        middle2 = a_list[int(n / 2)]
        total = middle1 + middle2
        median = total / 2
        return median

print(median([2, 3, 3, 6, 5, 9, 10, 100, 14, 17]))



