# 1673. Find the Most Competitive Subsequence
# Medium

# 540

# 36

# Add to List

# Share
# Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

# An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

# We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

 

# Example 1:

# Input: nums = [3,5,2,6], k = 2
# Output: [2,6]
# Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
# Example 2:

# Input: nums = [2,4,3,3,5,4,9,6], k = 4
# Output: [2,3,3,4]
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 1 <= k <= nums.length

# This solution works! - monoqueue:
class Solution:
    '''
    3 5 2 6 3
    k = 3
    
    canpop = 0
    num = 6
    monoq = [2,6,3]
    '''
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        monoq = []
        canpop = len(nums)-k
        for num in nums:
            while monoq and canpop and monoq[-1] > num:
                monoq.pop()
                canpop -= 1
            monoq.append(num)
        while len(monoq) > k:
            monoq.pop()
        return monoq
    
# This approach does not work - TLE:
# class Solution:
#     def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         def helper(arr, i):
#             if len(arr) == self.K:
#                 self.ans = min(self.ans, arr)
#                 return      
#             if i > len(nums)-1:
#                 return 
#             helper(arr + [nums[i]], i+1)
#             helper(arr, i+1)
            
#         self.K = k
#         self.ans = [float('inf') for _ in range(self.K)]
#         helper([], 0)
#         return self.ans

# This approach does not work - TLE:
# class Solution:
#     def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         def helper(arr, i):
#             if len(arr) == self.K:
#                 return arr      
#             ans = [float('inf') for _ in range(self.K)]
#             if i > len(nums)-1:
#                 return ans
#             ans = min(ans, helper(arr + [nums[i]], i+1))
#             ans = min(ans, helper(arr, i+1))
#             return ans
#         self.K = k
#         return helper([], 0)