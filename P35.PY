'''c1 : 33
c2 : 66
c3 : 1
'''
import math

def golf(clubs, target):
    distance = [0] + [math.inf] * target
    for current in range(len(distanes)):
        for c in clubs:
            new_loc = current + c
            if new_loc <= target:
                distances[new_loc] = min(distances[current]+1, distances[new_loc])
    return distances[target]

    