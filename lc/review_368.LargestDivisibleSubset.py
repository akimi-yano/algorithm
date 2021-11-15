# 368. Largest Divisible Subset
# Medium

# 2426

# 111

# Add to List

# Share
# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.
# Example 2:

# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 109
# All the integers in nums are unique.


# This solution works:


'''
First of all, notice, that if we need to find 3 numbers given properties, than if we put then in decreasing order a > b > c, than it is sufficient and enough that a%b = 0 and b%c=0, then it is automatically a%c=0.

Let us know sort our number and in sol[i] list keep the best solution, where the biggest number is equal to nums[i]. How can we find it? Look at all smaller numbers and if nums[i] is divisible by this smaller number, we can update solution. Let us go through example: nums = [4,5,8,12,16,20].

sol[0] = [4], the biggest divisible subset has size 1.
sol[1] = [5], because 5 % 4 != 0.
sol[2] = [4,8], because 8 % 4 = 0.
sol[3] = [4,12], because 12 % 4 = 0.
sol[4] = [4,8,16], because 16 % 8 = 0 and 16 % 4 = 0 and we choose 8, because it has longer set.
sol[5] = [4,20] (or [5,20] in fact, but it does not matter). We take [4,20], because it has the biggest length and when we see 5, we do not update it.
Finally, answer is [4,8,16].
Complexity: time complexity is O(n^2), because we fist sort our numbers and then we have double loop. Space complexity also potentially O(n^2), but for big n, length of the longest subset will not be more than 32: (each time you new number will be at least twice bigger than previous, so there will be maximum 32 numbers in our set) so so we can say it is O(32n).
'''
class Solution:
    def largestDivisibleSubset(self, nums):
        if len(nums) == 0: return []
        nums.sort()
        sol = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
                    sol[i] = sol[j] + [nums[i]]
        return max(sol, key=len)