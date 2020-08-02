# 238. Product of Array Except Self

# Given an array nums of n integers where n > 1,  return an array output such that output[i] is 
# equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the 
# array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra 
# space for the purpose of space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_memo = {}
        right_memo = {}
        def left_products(i):
            if i in left_memo:
                return left_memo[i]
            ans = 1
            if i < 1:
                pass
            else:
                ans = nums[i-1] * left_products(i-1)
            left_memo[i] = ans
            return ans

        def right_products(i):
            if i in right_memo:
                return right_memo[i]
            ans = 1
            if i >= len(nums)-1:
                pass
            else:
                ans = nums[i+1] * right_products(i+1)
            right_memo[i] = ans
            return ans

        ans = []
        for i in range(len(nums)):
            ans.append(left_products(i) * right_products(i))
        return ans
    
    # Time: O(N)
    # Space: O(N)
    

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numsLen = len(nums)
        productWithoutSelf = [1] * numsLen
        
        # productWithoutSelf[i] as product of elements to the left of nums[i].
        for i in range(1, numsLen):
            productWithoutSelf[i] = productWithoutSelf[i - 1] * nums[i - 1]
        
        # productWithoutSelf[i] multiply product of elements to the right of nums[i].
        rightProduct = 1
        for i in range(numsLen - 1, -1, -1):
            productWithoutSelf[i] *= rightProduct
            rightProduct = rightProduct * nums[i]
            
        return productWithoutSelf
    
    # Time: O(N)
    # Space: O(1)