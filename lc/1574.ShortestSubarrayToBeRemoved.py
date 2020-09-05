# 1574. Shortest Subarray to be Removed to Make Array Sorted
# Medium

# 71

# 2

# Add to List

# Share
# Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

# A subarray is a contiguous subsequence of the array.

# Return the length of the shortest subarray to remove.

 

# Example 1:

# Input: arr = [1,2,3,10,4,2,3,5]
# Output: 3
# Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
# Another correct solution is to remove the subarray [3,10,4].
# Example 2:

# Input: arr = [5,4,3,2,1]
# Output: 4
# Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
# Example 3:

# Input: arr = [1,2,3]
# Output: 0
# Explanation: The array is already non-decreasing. We do not need to remove any elements.
# Example 4:

# Input: arr = [1]
# Output: 0
 

# Constraints:

# 1 <= arr.length <= 10^5
# 0 <= arr[i] <= 10^9



# Ideas-the code is below:

# class Solution:
#     def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
#         '''
#         check from front and back or dp of remove/not_remove
#         '''
#         if len(arr)<2:
#             return 0
#         if arr == sorted(arr):
#             return 0


# This solution works ! :)

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        '''
        s1 e1 s2 e2
        |  |   | |  
        [oooxxxooo] - find the e1 and s2  
        edge case1: [xxxooo]
        edge case2: [oooxxx]
        edge case3: [oooooo]
        '''
        # 1 find e1
        e1 = -1
        for i in range(1, len(arr)):
            if arr[i]<arr[i-1]:
                e1 = i
                break
                
        # if e1 does not change, the whole array is already sorted -> return 0
        if e1 == -1:
            return 0
        
        s2 = len(arr)
        # 2 find s2
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>arr[i+1]:
                s2 = i+1
                break
                
        # 3 do sliding window for the best subarray to be removed
        best = len(arr)
        i = -1
        j = s2
        while i<e1:
            if j >= len(arr) or i < 0 or arr[i] <= arr[j]:
                best = min(best, j-i-1)
                i += 1
            # else, arr[i] is bigger than arr[j]; we need to move j up
            else:
                j += 1
        return best
                
        