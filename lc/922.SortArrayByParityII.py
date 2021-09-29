# 922. Sort Array By Parity II
# Easy

# 1418

# 65

# Add to List

# Share
# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

# Return any answer array that satisfies this condition.

 

# Example 1:

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# Example 2:

# Input: nums = [2,3]
# Output: [2,3]
 

# Constraints:

# 2 <= nums.length <= 2 * 104
# nums.length is even.
# Half of the integers in nums are even.
# 0 <= nums[i] <= 1000
 

# Follow Up: Could you solve it in-place?


# This solution works:


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        for num in nums:
            if num % 2:
                odds.append(num)
            else:
                evens.append(num)
        ans = []
        while evens and odds:
            ans.append(evens.pop())
            ans.append(odds.pop())
        return ans


# This solution works - optimization:

'''
O(n) space complexity soluiton is straightforward. It is more interseting to investigate O(1) solution. The idea is to use two pointers approach, where we start with index 0 for even numbers and with index 1 for odd numbers. We traverse our numbers, where we can have the following options:

if nums[i] % 2 == 0, then number is already on place, so we look at the next place for i.
if nums[j] % 2 == 1, then number is already on place, so we look ate the next place for j.
In the opposite case we need to sweich elements.
Complexity
Time complexity is O(n), space complexity is O(1).
'''

class Solution:
    def sortArrayByParityII(self, nums):
        i, j, n = 0, 1, len(nums)
        while j < n and i < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums