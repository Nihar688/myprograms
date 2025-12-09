#Input - (0,1,0,2,5)
#output- )1,2,5,0,0)
# given an integer array nums, move all 0's to the end of it whike maintaning the relative order of the non-zero elements
#must be done inplace without making. acopy of array

def zeroend(nums):
    zeroes = []
    non_zeroes = []
    for v in nums:
        if v == 0:
            zeroes.append(v)
        else:
            non_zeroes.append(v)

nums = non_zeroes + zeroes


    
def moveZeroes2(nums):
    temp = [0] * len(nums)
    i = 0
    for num in nums:
        if num != 0:
            temp[i] = num
            i += 1
    nums = temp