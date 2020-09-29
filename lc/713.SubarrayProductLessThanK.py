# 713. Subarray Product Less Than K
# Medium

# 1712

# 71

# Add to List

# Share
# Your are given an array of positive integers nums.

# Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

# Example 1:
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Note:

# 0 < nums.length <= 50000.
# 0 < nums[i] < 1000.
# 0 <= k < 10^6.



# This approach does not work - it TLEd !

# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         prefix_prod = []
#         prod = 1
#         count = 0
#         for num in nums:
#             prod *= num
#             prefix_prod.append(prod)
#             if prod < k:
#                 count += 1
        
#         for j in range(len(nums)):
#             for i in range(j+1,len(prefix_prod)):
#                 prefix_prod[i] = prefix_prod[i]//nums[j]
                
#                 if prefix_prod[i] < k:
#                     count += 1
#         return count


# This approach works !

'''
It is given that all numbers are natural, that is they are more or equal than 1. 
The idea is to use two pointers (or sliding window) approach, where at each moment of time we try to extend our window. 
Let us beg, end-1 be the beginning and end of our window (it means that if beg=end=0, our window is empty), 
P is current product of numbers in our window and out is our answer we need to return.

On each iteration, we extend our window by one number to the right: however we need to check first, 
that the product do not exceed k. 
So, we remove numbers from the beginning of our window, until product is less then k. 
Note also, that we can not have end < beg, so we break if it is the case: it means that our window becomes empty. 
Finally, we update out += end - beg + 1: this is number of subarrays ending with end with product less than k.

Complexity: time complexity is O(n), because on each step we increase either beg or end. Space complexity is O(1).
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        out, beg, end, P = 0, 0, 0, 1
        while end < len(nums):
            P *= nums[end]
            
            while end >= beg and P >= k:
                P /= nums[beg]
                beg += 1
                
            out += end - beg + 1
            end += 1
        return out
    
# Another approach which works !!!

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        N = len(nums)
        total = 0
        running = 1
        left = 0
        for right in range(N):
            running *= nums[right]
            
            while left < right and running >= k:
                running //= nums[left]
                left += 1
                
            if running < k:
                total += right - left + 1
        
        return total  
    
    
    

# This solution works ! explanation :) cool cool and happy
'''
fix the end by doing loop and move start if the prod is too large

if cur is too large - cannot go back to left because you are going to right (its just gonna be larger)and its accumulative

since there is no negative number or 0, its just gonna get bigger, so need to remove a number by division
'''


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = ans = 0
        prod =  1
        for end in range(len(nums)):
            prod *= nums[end]
            
            while start <= end and prod >= k:
                prod //= nums[start]
                start += 1
            
            ans += end - start +1 
        
        return ans 
