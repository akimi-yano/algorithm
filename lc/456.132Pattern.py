# 456. 132 Pattern
# Medium

# 1827

# 115

# Add to List

# Share
# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

# Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
# Example 2:

# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:

# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# -109 <= nums[i] <= 109


# This solution works !:
# Time: O(NlogN)
# Space: O(N)

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        pairs = []
        prefix = nums[0]
        for i in range(1, len(nums) - 1):
            cur = nums[i]
            if cur > prefix:
                new_pair = (prefix, cur)
                # first, remove any pairs that will be covered by the new pair
                while pairs:
                    old_pair = pairs[-1]
                    if new_pair[0] <= old_pair[0] <= old_pair[1] <= new_pair[1]:
                        pairs.pop()
                    else:
                        break
                pairs.append(new_pair)
            else:
                prefix = cur
            # print(pairs)
                
            third = nums[i+1]
            left, right = 0, len(pairs) - 1
            while left <= right:
                mid = (left + right) // 2
                first, second = pairs[mid]
                if first < third < second:
                    return True
                if first >= third:
                    left = mid + 1
                elif second <= third:
                    right = mid - 1
        return False