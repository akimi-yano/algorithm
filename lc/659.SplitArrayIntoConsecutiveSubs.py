# 659. Split Array into Consecutive Subsequences
# Medium

# 3696

# 721

# Add to List

# Share
# You are given an integer array nums that is sorted in non-decreasing order.

# Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

# Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
# All subsequences have a length of 3 or more.
# Return true if you can split nums according to the above conditions, or false otherwise.

# A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

 

# Example 1:

# Input: nums = [1,2,3,3,4,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,5] --> 1, 2, 3
# [1,2,3,3,4,5] --> 3, 4, 5
# Example 2:

# Input: nums = [1,2,3,3,4,4,5,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
# [1,2,3,3,4,4,5,5] --> 3, 4, 5
# Example 3:

# Input: nums = [1,2,3,4,4,5]
# Output: false
# Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
 

# Constraints:

# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000
# nums is sorted in non-decreasing order.


# This solution works:


class Solution:
    def isPossible(self, A):
        left = collections.Counter(A)
        end = collections.Counter()
        for i in A:
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True
 
        '''
        greedy algorithm.
        leftis a hashmap, left[i] counts the number of i that I haven't placed yet.
        endis a hashmap, end[i] counts the number of consecutive subsequences that ends at number i
        Then I tried to split the nums one by one.
        If I could neither add a number to the end of a existing consecutive subsequence nor find two following number in the left, I returned False

        Complexity
        Time O(N)
        Space O(N)
        '''

    