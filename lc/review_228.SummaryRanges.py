# 228. Summary Ranges
# Easy

# 1544

# 921

# Add to List

# Share
# You are given a sorted unique integer array nums.

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
 

# Constraints:

# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.


# This solution works:


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
        Input: nums = [0,1,2,4,5,7]
        Output: ["0->2","4->5","7"]
        Explanation: The ranges are:
        [0,2] --> "0->2"
        [4,5] --> "4->5"
        [7,7] --> "7"
        
        '''
        if not nums:
            return []
        arr = []
        prev = None
        for num in nums:
            if prev is None:
                temp = [str(num)]
            elif num-1 == prev:
                temp.append(str(num))
            else:
                arr.append(temp)
                temp = [str(num)]
            prev = num
        arr.append(temp)
        
        ans = []
        for sequence in arr:
            if len(sequence) <= 1:
                ans.append(sequence[0])
            else:
                ans.append(sequence[0] + "->" + sequence[-1])
        return ans
            

# This solution works - optimization:


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []
        ans = []
        prev = None
        for num in nums:
            if prev is None:
                start = end = str(num)
            elif num-1 == prev:
                end = str(num)
            else:
                if start == end:
                    ans.append(end)
                else:
                    ans.append(start + "->" + end)
                start = end = str(num)

            prev = num        
            
        if start == end:
            ans.append(end)
        else:                
            ans.append(start + "->" + end)

        return ans
            
