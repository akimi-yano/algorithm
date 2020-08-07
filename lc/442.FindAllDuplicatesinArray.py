# 442. Find All Duplicates in an Array

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]

# my solution  that works !

class Solution:
    def findDuplicates(self, nums) :
        ans = []
        for idx in nums:
        
            if nums[abs(idx)-1]>0:
                nums[abs(idx)-1]*=(-1)
            else:
                ans.append(abs(idx))

        return ans
    
    # 1<=elem<=n 
    # [4,3,2,7,8,2,3,1]
    #  0 1 2 3 4 5 6 7
      # -3-2-7-8ad-3-1
    

# explanations below ----

# O(1) space not including the input and output variables

# The idea is we do a linear pass using the input array itself as a hash to store which numbers have been seen before. We do this by making elements at certain indexes negative. See the full explanation here

# http://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

# Use array itself as hash map to store information.

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res
    

# Solution 1:

# Approach:The elements in the array is from 0 to n-1 and all of them are positive. 
# So to find out the duplicate elements, a HashMap is required, but the question is to solve the problem in constant space. 
# There is a catch, the array is of length n and the elements are from 0 to n-1 (n elements). The array can be used as a HashMap.



# 1 ≤ a[i] ≤ n (n = size of array)
# 1 - n
# 0 - n-1


# Algorithm:
# Traverse the array from start to end.
# For every element,take its absolute value and if the abs(array[i])‘th element is positive, the element has not encountered before, 
# else if negative the element has been encountered before print the absolute value of the current element.

# Implementation:

# Python3 code to find 
# duplicates in O(n) time 

# Function to print duplicates 
def printRepeating(arr, size): 
    ans =[]    
    for i in range(0, size): 
        if arr[abs(arr[i])] >= 0: 
            arr[abs(arr[i])] = -arr[abs(arr[i])] 
        else: 
            ans.append(abs(arr[i]))
    return ans
arr = [1, 2, 3, 1, 3, 6, 6]
print(printRepeating(arr,len(arr)))
            
    #   T diagram 
    #   [1,-2,-3,-1,x,x,6,-6]
    #              ad ad  ad 
    #              1  3   6 
    
    # using index and a dictionary and if you find it , change the val at the index to negatives 
    # if its negative, append to arr 
    
    
# arr = [1, 2, 3, 1, 3, 6, 6] 
# arr_size = len(arr) 

# printRepeating(arr, arr_size) 


# Note: The above program doesn’t handle 0 cases (If 0 is present in array). 
# The program can be easily modified to handle that also. It is not handled to keep the code simple.
# Complexity Analysis:
# Time Complexity: O(n), only one traversal is needed, so time complexity is O(n)
# Auxiliary Space: O(1), no extra space is required, so space complexity is constant.


# There is a problem in the above approach.
# It prints the repeated number more than once. For example: {1, 6, 3, 1, 3, 6, 6} it will give output as : 1 3 6 6. 
# In below set, another approach is discussed that prints repeating elements only once.

# Alternate Solution:

# Approach: The basic idea is to use a HashMap to solve the problem. 
# But there is a catch, the numbers in the array are from 0 to n-1, and the input array has length n. 
# So, the input array can be used as a HashMap. 
# While Traversing the array, if an element ‘a’ is encountered then increase the value of a%n‘th element by n. 
# The frequency can be retrieved by dividing the a % n’th element by n.

# Algorithm:
# Traverse the given array from start to end.
# For every element in the array increment the arr[i]%n‘th element by n.
# Now traverse the array again and print all those indexes i for which arr[i]/n is greater than 1. 
# Which guarantees that the number n has been added to that index
# This approach works because all elements are in the range from 0 to n-1 and arr[i] would be 
# greater than n only if a value “i” has appeared more than once.

# Implementation:

# Python3 code to find duplicates in O(n) time 

# this solution works for the case where there are duplicates more than (twice above!) once and 0 !

numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1, 3]; 
arr_size = len(numRay);  
def v2(numRay,arr_size):
    for i in range(arr_size): 
        res = []
        numRay[numRay[i] % arr_size] += arr_size
    # print(numRay)
    for i in range(arr_size): 
        if (numRay[i] >= arr_size*2):  
            res.append(i)
    return res 

print(v2(numRay,arr_size))

# Output:
# The repeating elements are : 
# 2 
# 3
# Complexity Anlaysis:
# Time Complexity: O(n).
# Only two traversals are needed. So the time complexity is O(n).
# Auxiliary Space: O(1).
# No extra space is needed, so the space complexity is constant.
# Duplicates in an array in O(n) and by using O(1) extra space | Set-2

