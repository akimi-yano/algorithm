# 645. Set Mismatch
# Easy

# 1015

# 406

# Add to List

# Share
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104

# This solution works:

from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        '''
        all choices:1 2 3 4  1 10 11 100
        real array: 1,2,2,4  1  2  3  4
                      - -
        xor = 2^3
        
            10 ^ 11 = 01
        
        1
        10, 100
        
        dup missing
        2,   3
        
        '''
        counts = Counter(nums)
        dup = None
        missing = None
        for num in range(1, n+1):
            if counts[num] < 1:
                missing = num
            elif counts[num] > 1:
                dup = num
        return [dup, missing]