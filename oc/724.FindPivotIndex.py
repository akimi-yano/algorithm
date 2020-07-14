# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/
# Given an array of integers, find the index where every element to the left sums up to
#  the same sum as every element to the right.
# Must be done in linear time and constant space.
# Example input 1: [3,2,5,4,9,1]  --. 
# output: 3

# The sum of elements to the left of index 3 (element 4) is 10. 
# The sum of elements to the right of index 3 (element 4) is 10.
# sum(3,2,5) == sum(9,1)
# Example input 2: [-1,-5,0,7,4,-4,4,1]
# output:

def pivot(arr):
    left_sum = 0
    right_sum = sum(arr)
    j=0
    while j<len(arr):
        right_sum-=arr[j]
        print(left_sum,right_sum)
        if left_sum == right_sum:
            return j
        left_sum+=arr[j]
        j+=1
    return -1
print(pivot([1,4,3,5]))