'''
2560. House Robber IV
Medium
Topics
Companies
Hint
There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

 

Example 1:

Input: nums = [2,3,5,9], k = 2
Output: 5
Explanation: 
There are three ways to rob at least 2 houses:
- Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
- Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
- Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
Therefore, we return min(5, 9, 9) = 5.
Example 2:

Input: nums = [2,7,9,3,1], k = 2
Output: 2
Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= (nums.length + 1)/2
'''

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        '''
        The key insight is that if the robber can steal from at least k houses with a capability of x, 
        then he can also do so with any capability > x. 
        Conversely, if he cannot steal from k houses with capability x, 
        then he cannot do so with any capability < x. This monotonicity makes the problem suitable for binary search.
        
        Check if it's possible to steal at least k houses.
        Create a greedy algorithm: always steal from the current house if its value is ≤ capability, 
        then skip the adjacent house.
        '''
        def can_steal_from_k_houses(min_val_stolen):
            num_house_stolen = 0
            i = 0
            while i < len(nums):
                if nums[i] <= min_val_stolen:
                    num_house_stolen += 1
                    i += 2
                else:
                    i += 1
            return num_house_stolen >= k

        left = min(nums)
        right = max(nums)

        while left < right:
            mid = (left + right) // 2
            if can_steal_from_k_houses(mid):
                right = mid
            else:
                left = mid + 1
        return left
       
        