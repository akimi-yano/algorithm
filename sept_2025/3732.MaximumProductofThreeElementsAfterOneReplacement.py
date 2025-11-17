'''
3732. Maximum Product of Three Elements After One Replacement
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

You must replace exactly one element in the array with any integer value in the range [-105, 105] (inclusive).

After performing this single replacement, determine the maximum possible product of any three elements at distinct indices from the modified array.

Return an integer denoting the maximum product achievable.

 

Example 1:

Input: nums = [-5,7,0]

Output: 3500000

Explanation:

Replacing 0 with -105 gives the array [-5, 7, -105], which has a product (-5) * 7 * (-105) = 3500000. The maximum product is 3500000.

Example 2:

Input: nums = [-4,-2,-1,-3]

Output: 1200000

Explanation:

Two ways to achieve the maximum product include:

[-4, -2, -3] → replace -2 with 105 → product = (-4) * 105 * (-3) = 1200000.
[-4, -1, -3] → replace -1 with 105 → product = (-4) * 105 * (-3) = 1200000.
The maximum product is 1200000.
Example 3:

Input: nums = [0,10,0]

Output: 0

Explanation:

There is no way to replace an element with another integer and not have a 0 in the array. Hence, the product of all three elements will always be 0, and the maximum product is 0.

 

Constraints:

3 <= nums.length <= 105
-105 <= nums[i] <= 105
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        abs_nums = sorted([(abs(num), num) for num in nums], reverse=True)[:3]
        min_abs = min(abs_nums, key=lambda x : x[0])[0]
        prod = 1
        used = False
        for abs_num, orig_num in abs_nums:
            if not used and abs_num == min_abs:
                used = True
                prod *= 10**5
            else:
                prod *= orig_num
        if prod < 0:
            prod *= -1

        return prod

# Another approach:

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # take the largest two absolute values in `nums`
        a, b = nlargest(2, map(abs, nums))
        return a * b * 10**5
    
# Another approach:

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # sort `nums` based on the absolute value of each number
        nums.sort(key=abs, reverse=True)
        return abs(nums[0]) * abs(nums[1]) * 10**5