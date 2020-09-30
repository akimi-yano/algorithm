# 41. First Missing Positive
# Hard

# 4242

# 861

# Add to List

# Share
# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1
# Follow up:

# Your algorithm should run in O(n) time and uses constant extra space.




# This solution solves all the test cases but its not constant space :
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = [i+1 for i in range(len(nums))]
        nums_set = set(nums)
        for num in missing:
            if num not in nums_set:
                return num
        return len(nums_set)+1 
        


# This solution works ! with Time: O(N) and Space: O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        all the values needs to be within the range of 1 - N+1
        loop1 turn neg,0, number larger than N into 1 so that all the numbers are now within 1 - N; also set a boolean has_one to see if we have one before flipping invalid numbers to 1
        loop2 use its index as the indicator if we saw the number idx = abs(val) - 1 -> flip the sign to - if the val at the idx is positive; we don't have to do anything if the sign is already negative  
        loop3 if the val negative its good - if the val is positive, return its idx +1;  
        if there is no negative found, return len + 1
        
        '''
        # step 1 
        N = len(nums)
        has_one = False
        for i, num in enumerate(nums):
            if num == 1:
                has_one = True
            elif not 1<=num<=N:
                nums[i] = 1
        if not has_one:
            return 1
        
        # step 2 
        for num in nums:
            idx = abs(num)-1
            if nums[idx]>0:
                nums[idx] *= (-1)
        
        # step 3 
        for i, num in enumerate(nums):
            if num>0:
                return i+1  
        
        return len(nums)+1
        