# 238. Product of Array Except Self

# Given an array nums of n integers where n > 1,  return an array output such that output[i] 
# is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the 
# array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra 
# space for the purpose of space complexity analysis.)



'''
Input:  [1,2,3,4]
Output: [24,12,8,6]

1) prod = 24
    [1,2,3,4]
    24//1,24//2,24//3,24//4
    24,12,8,6

2)  [1,2,6,24]
    1*orig 1*orig 2*
    []
    
3)  [1, 2, 3, 4]
     1                                       1*arr[0]     1*arr[0]*arr[1] 1**arr[0]*arr[1]*arr[2]
    [1,                                         1,               2,                6]
    ans[0]*1*arr[3]*arr[2]*arr[1]   ans[1]*1*arr[3]*arr[2]  ans[2]*1*arr[3]    ans[3]*1
    [24,                                        12,              8,                6]
    
'''

def prod_arr(arr):
    print(f"Before operations: {arr}")
    ans = [0]*len(arr)
    ans[0] = 1
    for i in range(1,len(arr)):
        ans[i] = ans[i-1]*arr[i-1]
    print(f"After the 1st path: {ans}")
    mult = 1 
    for i in range(len(arr)-1,-1,-1):
        ans[i] = mult * ans[i]
        mult *= arr[i]
    print(f"After the 2nd path: {ans}")
prod_arr([1,2,3,4])