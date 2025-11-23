'''
1262. Greatest Sum Divisible by Three
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:

1 <= nums.length <= 4 * 104
1 <= nums[i] <= 104
'''

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        r1, r2 = [], [] # Collect numbers with remainder 1 in r1, and remainder 2 in r2.
        total = 0 # Take the sum of all elements.

        for x in nums:
            total += x
            if x % 3 == 1:
                r1.append(x)
            elif x % 3 == 2:
                r2.append(x)

        # If sum % 3 == 0, return the sum.
        if total % 3 == 0:
            return total
        
        r1.sort()
        r2.sort()
        rem = total % 3

        if rem == 1:
            # If sum % 3 == 1:
            # ➤ Remove one smallest from r1 OR two smallest from r2.
            op1 = total - r1[0] if len(r1) >= 1 else 0
            op2 = total - r2[0] - r2[1] if len(r2) >= 2 else 0
        else: 
            # If sum % 3 == 2:
            # ➤ Remove one smallest from r2 OR two smallest from r1.
            op1 = total - r2[0] if len(r2) >= 1 else 0
            op2 = total - r1[0] - r1[1] if len(r1) >= 2 else 0

        # Choose the option with minimal loss, return the new sum.
        return max(op1, op2)