# 421. Maximum XOR of Two Numbers in an Array
# Medium

# 2811

# 258

# Add to List

# Share
# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

 

# Example 1:

# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.
# Example 2:

# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127
 

# Constraints:

# 1 <= nums.length <= 2 * 105
# 0 <= nums[i] <= 231 - 1


# This solution works:


class TreeNode:
    def __init__(self):
        self.left = None #1
        self.right = None #0

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        '''
        16,8,4,2,1
            1111
            
        3:  00011
        10: 01010
        5:  00101
        25: 11001
        2:  00010
        8:  01000
        '''
        root = TreeNode()
        for num in nums:
            cur = root
            for bit in range(30, -1, -1):
                if num & (1<<bit):
                    # go to left
                    if not cur.left:
                        cur.left = TreeNode()
                    cur = cur.left
                else:
                    # go to right
                    if not cur.right:
                        cur.right = TreeNode()
                    cur = cur.right
        best = 0
        for num in nums:
            cur = root
            xor = 0
            for bit in range(30, -1, -1):
                if num & (1<<bit):
                    # go to right
                    if cur.right:
                        xor = (xor << 1) | 1
                        cur = cur.right
                    else:
                        xor = xor << 1 
                        cur = cur.left
                else:
                    if cur.left:
                        xor = (xor << 1) | 1
                        cur = cur.left
                    else:
                        xor = xor << 1 
                        cur = cur.right
            best = max(best, xor)
        return best



