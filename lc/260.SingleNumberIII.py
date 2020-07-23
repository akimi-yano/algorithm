# 260. Single Number III
# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
# Find the two elements that appear only once.

# Example:

# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# Note:

# The order of the result is not important. So in the above example, [5, 3] is also correct.
        
def singleNumber(nums):
    xor = 0
    a = 0
    b = 0
    for num in nums:
        xor ^= num
    # print(bin(xor)) # 6
    
    mask = 1
    # print(bin(mask)) # 1
    
    # 110 - xor
    #   1 - mask
    # --- &
    #   0 (=0)
    # -> mask <<1 
    # 10 - mask

    # 110 - xor
    #  10 -  mask
    # --- &
    #  10 = 2 (=!0) gets out of the while loop
    
    while(xor&mask == 0):
        mask = mask << 1
        # print(bin(mask))
        # print(bin(xor))
        # print(xor&mask)
    
    # mask = '10' = 2 
    for num in nums:
        if num&mask: # True - means there is only one common digit of both xor
            a ^= num
        else: # False
            b ^= num
    return [a, b]
print(singleNumber([1, 2, 1, 3, 2, 5]))

# a group:
# 2 = 010
    #  10
    #  10 - True 
# 2 = 010
    # same - True
# 3 = 011
    #  10
    #  10 - True

# b group:
# 1 = 001
    #  10
    # 000 - False 
# 1 = 001
    # same -  False
# 5 = 101
    #  10
    #  00 - False
    
    
# after 1st step, we found out that a^b = 3^5 = 6 which is 110
# 110 means that there are 2 digits on the left are different in binary representation of our result
# let's use any one of the digit to partition our array

# if we use the middle one, we can see that there are 2 sets of numbers that we can just use the simple single number to find out the single in each partition
# 1 = 001
# 1 = 001
# 5 = 101 ✅
# 2 = 010
# 2 = 010
# 3 = 011 ✅

# if we use the leftmost one, we can still partition the array into the sets and do simple single number on it
# 1 = 001
# 2 = 010
# 1 = 001
# 3 = 011✅
# 2 = 010
# 5 = 101✅