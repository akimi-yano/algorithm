# 376. Wiggle Subsequence
# Medium

# 1325

# 67

# Add to List

# Share
# A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

# For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

# Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

# Example 1:

# Input: [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence.
# Example 2:

# Input: [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
# Example 3:

# Input: [1,2,3,4,5,6,7,8,9]
# Output: 2
# Follow up:
# Can you do it in O(n) time?


# This solution works:


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        '''
        [1, 7, 4, 9, 2, 5]
          +6 -3 +5 -7 +3
          
         
        [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
         +16  -12 +5 +3  -2  -5  -5 +11 -8
         
         if len(nums) is 0 then return 0
         if len(nums) is 1 then return 1
         
         0 is not ok 
         check each element and keep track of the previous val
         compare differences to see if they are positive or negative 
         keep track whether current one is positive or negative
         keep track of counts that we want to remove
         reutrn the length of array - removed
        '''
        if len(nums) < 2:
            return len(nums)
        is_positive = None
        prev = nums[0]
        removed = 0
        for i in range(1, len(nums)):
            if (nums[i] - prev) == 0:
                removed += 1
            elif (nums[i] - prev) > 0:
                if is_positive is True:
                    removed += 1
                else:
                    is_positive = True
            else:
                if is_positive is False:
                    removed += 1
                else:
                    is_positive = False
            
            prev = nums[i]
            
        return len(nums) - removed