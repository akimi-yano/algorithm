# 1675. Minimize Deviation in Array
# Hard

# 665

# 34

# Add to List

# Share
# You are given an array nums of n positive integers.

# You can perform two types of operations on any element of the array any number of times:

# If the element is even, divide it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
# If the element is odd, multiply it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
# The deviation of the array is the maximum difference between any two elements in the array.

# Return the minimum deviation the array can have after performing some number of operations.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: 1
# Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
# Example 2:

# Input: nums = [4,1,5,20,3]
# Output: 3
# Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
# Example 3:

# Input: nums = [2,10,8]
# Output: 3
 

# Constraints:

# n == nums.length
# 2 <= n <= 105
# 1 <= nums[i] <= 109


# This solution works:


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # use minheap
        heap = []
        
        # if the value is even, devide by 2 and put them into heap and keep track of max_val 
        max_val = 0
        for num in nums:
            divided_val = num
            while divided_val % 2 == 0:
                divided_val //= 2
            heapq.heappush(heap, (divided_val, num))
            max_val = max(max_val, divided_val)
        
        
        # pop from heap and keep track of minimum value (ans)
        # if its odd or even but has not reached the original value, multiply by 2 and push back to heap
        # else return ans
        
        ans = float('inf')
        while heap:
            divided_val, num = heapq.heappop(heap)
            ans = min(ans, max_val - divided_val)
            if divided_val % 2 == 1 or divided_val < num:
                divided_val *= 2
                heapq.heappush(heap, (divided_val, num))
                max_val = max(max_val, divided_val)
            else:
                return ans