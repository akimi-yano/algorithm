# 152. Maximum Product Subarray
# Medium

# 4898

# 172

# Add to List

# Share
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    #     min_so_far = max_so_far = best = nums[0]
    #     for num in nums[1:]:
    #         min_so_far, max_so_far = min(num, min_so_far * num, max_so_far * num), max(num, min_so_far * num, max_so_far * num)
    #         best = max(best, max_so_far)
    #     return best
    
    def maxProduct(self, nums: List[int]) -> int:
        minprod = maxprod = best = nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                minprod,maxprod = maxprod,minprod
            maxprod = max(maxprod*nums[i],nums[i])
            minprod = min(minprod*nums[i],nums[i])
            best  = max(best,maxprod)
        return best
    

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # initialize the max,min,best to as the first elem in the arr
        max_prod = min_prod = best = nums[0]
        # skip the first elem as we already checked in the prevous step 
        for i in range(1,len(nums)):
            # compare and get the global max and min - could be previous one * cur_num or just cur_num 
            max_prod, min_prod = max(max_prod*nums[i], nums[i],min_prod*nums[i]), min(min_prod*nums[i], nums[i],max_prod*nums[i])
            # compare best with max
            best = max(best, max_prod)
        return best 
    
    
    
# More intuitive way 

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        2 paths solution
        reset cur to 1 if I get 0
        if its negative, keep going
        there are only 2 patterns and 1 generic one:
        [xxxooo]
        [oooxxx]
        [oooooo] (generic one)
        '''
        best = nums[0]
        cur = 1
        for i in range(len(nums)):
            cur *= nums[i]
            best = max(best, cur)
            if cur == 0:
                cur = 1
        
        cur = 1
        for k in range(len(nums)-1,-1,-1):
            cur*=nums[k]
            best = max(best,cur)
            if cur == 0:
                cur = 1
                
        return best
