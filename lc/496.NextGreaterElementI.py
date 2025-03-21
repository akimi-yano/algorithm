# 496. Next Greater Element I
# Easy

# 1804

# 2356

# Add to List

# Share
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
#     For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
#     For number 1 in the first array, the next greater number for it in the second array is 3.
#     For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
#     For number 2 in the first array, the next greater number for it in the second array is 3.
#     For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
# Note:
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.


# THIS SOLUTION WORKS ! 
'''
iterate  through the nums1 arr and find the number at nums2 and go  to right to  find any larger number from the spot of the  num
don't forget to break once you find one 
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo = {}
        for i,num in enumerate(nums2):
            memo[num] = i
        
        ans = []
        for i,num in enumerate(nums1):
            idx = memo[num]
            val = -1
            for k in range(idx,len(nums2)):
                if nums2[k]>num:
                    val = nums2[k]
                    break
            ans.append(val)
        return ans