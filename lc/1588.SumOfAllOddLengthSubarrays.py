# 1588. Sum of All Odd Length Subarrays
# Easy

# 20

# 1

# Add to List

# Share
# Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

# A subarray is a contiguous subsequence of the array.

# Return the sum of all odd-length subarrays of arr.

 

# Example 1:

# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
# Example 2:

# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
# Example 3:

# Input: arr = [10,11,12]
# Output: 66
 

# Constraints:

# 1 <= arr.length <= 100
# 1 <= arr[i] <= 1000

# this approach works but less intuitive and harder to prove :

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1):
                if (i+j)%2!=0:
                    total+=sum(arr[i:j]) 
        return total
    
    
# this approach works and intuitive :

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if (j-i+1)%2!=0:
                    total+=sum(arr[i:j+1]) 
        return total
    
    
    
    
    '''
Solution 2: Consider the contribution of A[i]

Consider the subarray that contains A[i],
we can take 0,1,2..,i elements on the left, we have i + 1 choices.
we can take 0,1,2..,n-1 elements on the right, we have n - i choices.

In total, there are (i + 1) * (n - i) subarrays, that contains A[i].
And there are ((i + 1) * (n - i) + 1) / 2 subarrays with odd length, that contains A[i].
A[i] will be counted ((i + 1) * (n - i) + 1) / 2 times.

Complexity, time O(N), space O(1)
'''

    def sumOddLengthSubarrays(self, A):
        res, n = 0, len(A)
        for i, a in enumerate(A):
            res += ((i + 1) * (n - i) + 1) // 2 * a
        return res
'''
 i+1   i   n-i
[... , a , ...]

length before i * length after i * the value a 
and divide it by 2 to get odds

(i+1) * (n-i) * a
-----------------
        2

'''



    def sumOddLengthSubarrays(self, A):
        return sum(((i + 1) * (len(A) - i) + 1) / 2 * a for i, a in enumerate(A))