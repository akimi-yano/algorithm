# 453. Minimum Moves to Equal Array Elements
# Easy

# 764

# 1110

# Add to List

# Share
# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

# In one move, you can increment n - 1 elements of the array by 1.



# Example 1:

# Input: nums = [1,2,3]
# Output: 3
# Explanation: Only three moves are needed (remember each move increments two elements):
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# Example 2:

# Input: nums = [1,1,1]
# Output: 0


# Constraints:

# n == nums.length
# 1 <= nums.length <= 104
# -109 <= nums[i] <= 109


# This approach does not work:


# import heapq
# class Solution:
#     def minMoves(self, nums: List[int]) -> int:
#         max_num = max(nums)
#         count = 0
#         minheap = []
#         for num in nums:
#             heapq.heappush(minheap, num)
#         while max_num != minheap[0]:
#             smallest = heapq.heappop(minheap)
#             diff = max_num - smallest
#             count += diff
#             temp = []
#             temp.append(smallest+diff)
#             second = float('-inf')
#             while len(minheap) > 1:
#                 second = heapq.heappop(minheap)
#                 temp.append(second+diff)
            
#             max_num = max(max_num, second+diff)
#             while temp:
#                 heapq.heappush(minheap, temp.pop())
            
#         return count



# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/discuss/93817/It-is-a-math-question

'''
A more natural way to think about this question:
there is a staircase on which every numbers in array stand with corresponding step. '1' is on the 1st step and '5' on the 5th step.

A single move makes n-1 numbers step up, while on the other hand, we can also think a move as the remaining one step down. The relative distance between the numbers are same.

Our goal is to make all numbers on the same step.
Rather than move n-1 numbers up every time, why not just move one number down?

so the problem is simple:

find the min
move other numbers down to min.
number of moves = nums[0]-min + nums[1]-min + .... +nums[n]-min = sum - n * min

just another way to think of the magic equation.
'''

# This solution works:

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums)*len(nums)
        