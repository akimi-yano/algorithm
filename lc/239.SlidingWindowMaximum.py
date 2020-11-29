# 239. Sliding Window Maximum
# Hard

# 4584

# 201

# Add to List

# Share
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Example 3:

# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# Example 4:

# Input: nums = [9,11], k = 2
# Output: [11]
# Example 5:

# Input: nums = [4,-2], k = 2
# Output: [4]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

# This approach does not work :

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         prefix_max = {}
#         cur_max = nums[0]
#         prefix_max[0] = cur_max
#         for i in range(1, len(nums)):
#             cur_max = max(cur_max, nums[i])
#             prefix_max[i] = cur_max 
        
#         # print(prefix_max)
#         ans = []
#         for start in range(len(nums)):
#             end = k+start
#             if end > len(nums):
#                 break
#             ans.append(max(nums[start:end]))
#         return ans

# This solution works !:
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Keep indexes of good candidates in deque queue. The indexes in d are from the current window,
        # they're increasing, and their corresponding nums are decreasing. 
        # Then the first deque element is the index of the largest window value.
        # For each index i:
        # Pop (from the end) indexes of smaller elements (they'll be useless).
        # Append the current index.
        # Pop (from the front) the index i - k, if it's still in the deque 
        # (it falls out of the window).
        # If our window has reached size k, append the current window maximum to the output.
        
        queue = deque()
        ans = []
        for i, val in enumerate(nums):
            # smaller vals (s' indexes) than the current val are removed
            while queue and nums[queue[-1]] <= val:
                queue.pop()
            # append the current index 
            queue.append(i)
            # if the left most in the queue is supposed to be fall out, fall out
            if queue[0] == i - k:
                queue.popleft()
            # to ignore the first a couple indexes/ elems before it hits k 
            if i >= k - 1:
                ans.append(nums[queue[0]])
        return ans