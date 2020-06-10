
# //Minimum Size Subarray Sum

# Given an array of n positive integers and a positive integer s, 
# find the minimal length of a contiguous subarray of which the sum ≥ s. 
# If there isn't one, return 0 instead.

# https://leetcode.com/problems/minimum-size-subarray-sum/
"""
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem 
constraint.

Questions to ask:
any constrains ? - no 
time complexity ? - O(N)
space complexity ? - O(1)

different example to make sure that I understand the problem :
input: s = 5, nums = [1,2,3,4,5]
                        l r
            min_length = min(min_length,(r-l+1))
            sum-= nums[l]
            move the r if its smaller than s
output: 1 
as 5 itself is greater than or equal to 5

"""
def minSubArr(nums,s):
    min_length = len(nums)
    left = 0
    right = 0
    sum = 0 
    while right<len(nums):
        sum += nums[right]
        right+=1

        while sum>=s:
            min_length = min(min_length,(right-1-left+1))
            sum-=nums[left]
            left+=1
    if left == 0 and min_length == len(nums):
        return 0
    return min_length
print(minSubArr([1,2,3,4,5],5))
print(minSubArr([2,3,1,2,4,3],7))
